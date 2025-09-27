"""
Falcon-LLM Module

Provides a simplified API for using Falcon-LLM in integration scripts.
"""

from typing import Optional, Dict, Any
import warnings

def initialize_model(model_name: str = "tiiuae/falcon-7b", **kwargs) -> Optional[Any]:
    """
    Initialize a Falcon model.
    
    Args:
        model_name: Name of the model to load
        **kwargs: Additional arguments for model initialization
        
    Returns:
        Initialized model or None if dependencies not available
    """
    try:
        from model_hfport import FalconForCausalLM
        from transformers import AutoTokenizer
        import torch
        
        model = FalconForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.bfloat16,
            device_map="auto",
            **kwargs
        )
        
        tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        tokenizer.pad_token = tokenizer.eos_token
        
        return {"model": model, "tokenizer": tokenizer}
        
    except ImportError as e:
        warnings.warn(f"Could not initialize Falcon model: {e}")
        return None

def generate_text(prompt: str, model_data: Optional[Dict] = None, max_length: int = 200, **kwargs) -> str:
    """
    Generate text using Falcon-LLM.
    
    Args:
        prompt: Input text prompt
        model_data: Dictionary containing model and tokenizer
        max_length: Maximum length of generated text
        **kwargs: Additional generation parameters
        
    Returns:
        Generated text
    """
    if model_data is None:
        return f"[Placeholder] Generated response for: {prompt}"
    
    try:
        import torch
        from transformers.trainer_utils import set_seed
        
        model = model_data["model"]
        tokenizer = model_data["tokenizer"]
        
        inputs = tokenizer(prompt, return_token_type_ids=False, return_tensors="pt")
        
        # Move to appropriate device if CUDA is available
        if torch.cuda.is_available():
            inputs = inputs.to("cuda")
        
        with torch.no_grad():
            set_seed(42)  # For reproducible results
            outputs = model.generate(
                **inputs,
                max_length=max_length,
                temperature=kwargs.get('temperature', 1.0),
                do_sample=kwargs.get('do_sample', True),
                top_k=kwargs.get('top_k', 50),
                early_stopping=kwargs.get('early_stopping', True),
            )
        
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return generated_text
        
    except Exception as e:
        warnings.warn(f"Error generating text: {e}")
        return f"[Error] Could not generate text for: {prompt}"

class FalconLLM:
    """Simple wrapper class for Falcon-LLM functionality."""
    
    def __init__(self, model_name: str = "tiiuae/falcon-7b"):
        """Initialize the Falcon-LLM wrapper."""
        self.model_name = model_name
        self.model_data = None
        self._initialized = False
    
    def initialize(self):
        """Initialize the model (lazy loading)."""
        if not self._initialized:
            self.model_data = initialize_model(self.model_name)
            self._initialized = True
        return self.model_data is not None
    
    def generate(self, prompt: str, **kwargs) -> str:
        """Generate text for the given prompt."""
        if not self._initialized:
            self.initialize()
        
        return generate_text(prompt, self.model_data, **kwargs)
    
    def is_available(self) -> bool:
        """Check if the model is available and properly initialized."""
        return self.model_data is not None

# Convenience function for simple usage
def main():
    """Main function that can be imported by integration scripts."""
    return FalconLLM()