# Baby's First Computer - Web Version

## Project Overview

- **Name**: Baby First Computer
- **Type**: Color Game (Web). Interactive screen experience for pre-walking/talking babies
- **Core functionality**: Fullscreen solid-color display that changes on any keypress
- **Target users**: Babies (pre-verbal, pre-mobile) with parent supervision

## Visual Specification

### Display
- Fullscreen mode (covers entire viewport)
- Single solid color fill covering entire screen
- No UI elements, text, or graphics
- High-contrast colors suitable for infant vision

### Color Palette (8 colors)
Cycle through these colors in order:
1. Bright Red `#FF0000`
2. Bright Green `#00FF00`
3. Bright Blue `#0000FF`
4. Yellow `#FFFF00`
5. White `#FFFFFF`
6. Black `#000000`
7. Pink `#FFB6C1` (light pink)
8. Cyan `#00FFFF`

### Behavior
- Initial color: White
- Each keypress advances to the next color in the list
- Color wraps around (after last color, returns to first)
- Color stays solid with no transitions or animations

## Audio Specification

### Sound Effects
- Each color has an associated musical tone (simple sine wave via Web Audio API)
- Tone plays immediately when color changes
- Frequencies mapped to create a pleasant ascending scale:
  1. Red: C4 (261 Hz)
  2. Green: E4 (330 Hz)
  3. Blue: G4 (392 Hz)
  4. Yellow: C5 (523 Hz)
  5. White: E5 (659 Hz)
  6. Black: G5 (784 Hz)
  7. Pink: C6 (1047 Hz)
  8. Cyan: E6 (1319 Hz)

### Audio Parameters
- Duration: 200ms
- Envelope: Quick fade-out to avoid clicks
- Volume: Comfortable default level

## Interaction Specification

### Controls
- **Any keypress**: Cycle to next color + play tone
- **ESC key**: Exit fullscreen mode (browser default) or quit prompt

### Exit Behavior
- ESC key exits fullscreen (browser default)
- Browser close button exits
- Returns to normal browsing

## Technical Requirements

- Modern browser with Web Audio API support
- No external dependencies
- Single HTML file with embedded CSS and JS

## Acceptance Criteria

1. Page loads in fullscreen or can enter fullscreen
2. Screen displays solid white initially
3. Pressing any key changes color to next in sequence
4. Each color change plays corresponding tone
5. ESC key exits fullscreen mode
