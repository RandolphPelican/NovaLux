import random

def glitch_text(text):
    words = text.split()
    glitched_output = []
    
    for word in words:
        # 12% chance to stutter to mimic the Max Headroom glitch
        if random.random() < 0.12 and len(word) > 3:
            stutter = (word[:2] + "-") * random.randint(1, 2)
            glitched_output.append(stutter + word)
        else:
            glitched_output.append(word)
            
    return " ".join(glitched_output)

if __name__ == "__main__":
    sample = "Welcome to the Nova Lux Association. The transition is now."
    print("\nOriginal: " + sample)
    print("Glitched: " + glitch_text(sample) + "\n")
