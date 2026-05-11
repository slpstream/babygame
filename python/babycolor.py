#!/usr/bin/env python3
"""
Baby Color Game
A simple fullscreen color cycling game for babies.
Press any key to change colors, ESC to quit.
"""

import pygame
import numpy as np

def main():
    # Initialize pygame
    pygame.init()
    pygame.mixer.init()

    # Display setup - get current screen resolution
    screen_info = pygame.display.Info()
    screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h))
    pygame.display.toggle_fullscreen()

# Color palette with RGB values
    COLORS = [
        (255, 0, 0),       # Red
        (0, 255, 0),       # Green
        (0, 0, 255),       # Blue
        (255, 255, 0),     # Yellow
        (255, 255, 255),   # White
        (0, 0, 0),         # Black
        (255, 182, 193),   # Pink
        (0, 255, 255),     # Cyan
    ]

    # Frequencies for each color (C4, E4, G4, C5, E5, G5, C6, E6)
    FREQUENCIES = [261, 330, 392, 523, 659, 784, 1047, 1319]

    # Audio settings
    SAMPLE_RATE = 44100
    TONE_DURATION = 0.2  # 200ms

    # Current color index
    current_index = 4  # Start with White

    # Pre-generate tones for each color
    tones = []
    for freq in FREQUENCIES:
        samples = int(SAMPLE_RATE * TONE_DURATION)
        t = np.linspace(0, TONE_DURATION, samples, False)
        # Generate sine wave with fade-out envelope
        wave = np.sin(2 * np.pi * freq * t)
        # Apply envelope to avoid clicks
        envelope = np.exp(-t * 10)
        wave = wave * envelope
        # Convert to 16-bit audio
        wave = (wave * 32767 * 0.5).astype(np.int16)
        # Create stereo sound
        stereo_wave = np.column_stack((wave, wave))
        sound = pygame.sndarray.make_sound(stereo_wave)
        tones.append(sound)

    # Fill screen with initial color (White)
    screen.fill(COLORS[current_index])
    pygame.display.flip()

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    # Any other key: cycle to next color
                    current_index = (current_index + 1) % len(COLORS)
                    screen.fill(COLORS[current_index])
                    pygame.display.flip()
                    # Play corresponding tone
                    try:
                        tones[current_index].play()
                    except pygame.error:
                        # Ignore audio errors (e.g., no audio device)
                        pass

    # Clean exit
    pygame.quit()

if __name__ == "__main__":
    main()
