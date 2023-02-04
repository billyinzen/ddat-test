from func import RelativeTimeModifier
from datetime import datetime
import sys

def parse(value: str) -> datetime:
    return RelativeTimeModifier.parse(value)

if __name__ == "__main__":
    args = sys.argv[1:]
    
    if len(args) == 0:
        raise TypeError(f"Relative time modifier requires at least one argument ({len(args)} given)")
    
    for arg in args:
        dt = parse(arg)
        print(dt.strftime("%Y-%m-%dT%H:%M:%SZ"), '\t', arg)
        
    
