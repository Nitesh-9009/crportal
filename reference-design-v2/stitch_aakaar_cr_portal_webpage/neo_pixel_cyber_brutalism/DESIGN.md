---
name: Neo-Pixel Cyber-Brutalism
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0edec'
  surface-container-high: '#ebe7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#4e4632'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#80765f'
  outline-variant: '#d2c5ab'
  surface-tint: '#745b00'
  primary: '#745b00'
  on-primary: '#ffffff'
  primary-container: '#ffcc00'
  on-primary-container: '#6f5700'
  inverse-primary: '#f1c100'
  secondary: '#006970'
  on-secondary: '#ffffff'
  secondary-container: '#00eefc'
  on-secondary-container: '#00686f'
  tertiary: '#ab3500'
  on-tertiary: '#ffffff'
  tertiary-container: '#ffc5b3'
  on-tertiary-container: '#a43200'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffe08b'
  primary-fixed-dim: '#f1c100'
  on-primary-fixed: '#241a00'
  on-primary-fixed-variant: '#584400'
  secondary-fixed: '#7df4ff'
  secondary-fixed-dim: '#00dbe9'
  on-secondary-fixed: '#002022'
  on-secondary-fixed-variant: '#004f54'
  tertiary-fixed: '#ffdbd0'
  tertiary-fixed-dim: '#ffb59d'
  on-tertiary-fixed: '#390c00'
  on-tertiary-fixed-variant: '#832600'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  headline-xl:
    fontFamily: Space Mono
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
  headline-xl-mobile:
    fontFamily: Space Mono
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
  headline-lg:
    fontFamily: Space Mono
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Space Mono
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  headline-md:
    fontFamily: Space Mono
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  headline-sm:
    fontFamily: Space Mono
    fontSize: 20px
    fontWeight: '700'
    lineHeight: 28px
  body-lg:
    fontFamily: Space Mono
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
  body-md:
    fontFamily: Space Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
  body-sm:
    fontFamily: Space Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
  label-lg:
    fontFamily: Space Mono
    fontSize: 14px
    fontWeight: '700'
    lineHeight: 20px
  label-md:
    fontFamily: Space Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
  label-sm:
    fontFamily: Space Mono
    fontSize: 10px
    fontWeight: '700'
    lineHeight: 14px
spacing:
  gutter: 1.5rem
  gutter-sm: 1rem
  margin: 2rem
  margin-sm: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style
This design system fuses 8-bit / 16-bit arcade pixel aesthetics with neo-brutalist structure. Designed for technical youth demographics, campus leaders, and engineering festivals, it channels the tactile energy of classic video game HUDs (Heads-Up Displays), technical drafting blueprints, and bold retro-futurism. 

The mood is irreverent, sharp, tactile, and highly energetic. High-contrast thick black outlines, razor-sharp 0px geometry, crisp hard-angled drop shadows, and graph-paper canvas grids create a physical, modular surface that feels like an interactive arcade console crossed with a technical blueprint.

## Colors
The palette is rooted in arcade nostalgia with electric, saturated primaries against neutral drafting backgrounds:

- **Primary (`#FFCC00`):** Arcade Gold/Amber. Applied to key interactive triggers, active tab states, primary callouts, and milestone progress.
- **Secondary (`#00F0FF`):** Cyber Cyan. Used for technical telemetry, live indicators, secondary actions, and high-impact tags.
- **Tertiary (`#FF6B35`):** Retro Neon Orange. Deployed for urgent alerts, critical notifications, energy metrics, and streak counters.
- **Neutral (`#121212`):** Carbon Ink Black. Forms all hard boundaries, structural divider lines, pixel borders, text headlines, and non-diffused hard shadows.
- **Canvas (`#FAF8F5`):** Warm Graph Paper. Rendered with faint grey blueprint grids (`#E2DFD8` repeating at 16px increments).
- **Accents:** Neon Green (`#39FF14`) for success states and XP gains; Arcade Magenta (`#FF007F`) for competitive rankings and leaderboard badges.

## Typography
Typographic rhythm relies on monospaced geometry. Space Mono enforces structural alignment and terminal-inspired precision across all content types.

- **Headlines:** Set in uppercase or capitalized sentence case with heavy weighting (`700`). Pixel headings must feel machine-carved, maintaining strict horizontal rhythm and generous vertical clearance.
- **Body:** Monospaced regular (`400`) delivers technical readability while sustaining the digital drafting aesthetic.
- **Labels & Tags:** Uppercase `700` weight with subtle tracking (`+0.05em`) for HUD metrics, rank indicators, and tab descriptors.

## Layout & Spacing
The layout adheres strictly to an 8-bit modular scale based on 8px and 16px increments. 

- **Grid Canvas:** A 12-column layout on desktop screens (1024px+) with a fixed max-width container of 1280px, flanked by graph-paper patterned canvas margins.
- **Breakpoints:**
  - `Mobile` (< 768px): 4-column grid, compact 16px margins, stacked cards, full-width button rows.
  - `Tablet` (768px - 1023px): 8-column grid, 24px margins, dual-column cards.
  - `Desktop` (1024px+): 12-column grid, 32px margins, multi-pane HUD arrangement.
- **Rhythm:** Every gap, margin, and padding dimension must resolve to multiples of 4px and 8px to guarantee pixel snap across low-DPI and high-DPI displays alike.

## Elevation & Depth
Depth is completely tactile, directional, and physical. Soft blurred shadows, ambient glows, and gradients are strictly prohibited. Depth is achieved via hard neo-brutalist offset blocks:

- **Border Standard:** Every interactive boundary, card container, and floating module features a solid `2px` or `3px` solid `#121212` border.
- **Level 1 (Resting Cards & Tabs):** `box-shadow: 4px 4px 0px #121212;`
- **Level 2 (Active Modals, Hero Panels, Floating HUDs):** `box-shadow: 6px 6px 0px #121212;`
- **Level 3 (Max Elevation / Flyouts):** `box-shadow: 8px 8px 0px #121212;`
- **Interactive States:** On `:hover`, components depress slightly by reducing the shadow to `2px 2px 0px #121212` with a `translate(2px, 2px)` transform. On `:active` (click/press), the transform reaches `translate(4px, 4px)` with `box-shadow: 0px 0px 0px #121212;`, simulating a physical arcade button being fully depressed into the board.

## Shapes
Sharpness is absolute. All UI components have `border-radius: 0px`. 

Corners must be orthogonal and uncompromising to mimic rasterized pixel graphics and raw structural civil scaffolding. In rare cases where corner styling is desired (such as pixelated badges or arcade health bars), simulate stepped pixel notches via CSS clip-paths rather than rounding geometry.

## Components

### Buttons
- **Primary:** Background `#FFCC00`, 3px solid `#121212` border, `4px 4px 0 #121212` drop shadow, label in Space Mono bold uppercase. Hover animates `translate(2px, 2px)` with shadow reducing to `2px 2px 0 #121212`.
- **Secondary:** Background `#FFFFFF`, 3px solid `#121212` border, `4px 4px 0 #121212` shadow.
- **Ghost/Tertiary:** Background transparent, 2px solid `#121212`, no resting shadow, active fill `#00F0FF` on hover.

### Tab Navigation (HUD Header)
- Segmented block tabs joined directly to bottom header borders.
- Inactive tabs: Background `#FFFFFF`, 2px solid `#121212`, top-border aligned, text in black.
- Active tab: Background `#FFCC00`, 3px solid `#121212`, overlapping the lower frame with a persistent `4px 4px 0 #121212` depth offset. Includes an optional 8-bit glyph/icon prefix.

### Cards & Modules
- Enclosed with 3px solid `#121212`, white or graph-paper tinted background (`#FAF8F5`), and standard `4px 4px 0px #121212` shadow.
- Optional top-accent banner bar: 28px height header strip filled in `#FFCC00`, `#00F0FF`, or `#FF6B35` containing the card's category tag in monospaced bold text.

### Inputs & Form Controls
- **Text Inputs:** Background `#FFFFFF`, 2px solid `#121212`, 0px border-radius, padded 12px 16px. On focus: thick 3px solid `#121212` outline with an instantaneous `3px 3px 0 #00F0FF` highlight shadow.
- **Checkboxes & Radios:** Sharp square boxes (20x20px), 2px solid `#121212`. Checked state fills the box with `#FFCC00` and a centered black pixel square (8x8px) for selection.

### Progress Bars (8-Bit Segmented Meters)
- Outer container: 20px height, 2px solid `#121212`, background `#E2DFD8`.
- Fill track: Solid `#FFCC00` or `#39FF14`, segmented into distinct stepped blocks using a dashed border or a CSS stepped gradient to mimic retro health/XP meters.

### Badges & Pill Tags
- Sharp rectangular labels with 2px solid `#121212` borders.
- Backgrounds in high-contrast primaries (`#FF6B35`, `#00F0FF`, `#39FF14`), text set in bold uppercase monospace at 10px or 12px.