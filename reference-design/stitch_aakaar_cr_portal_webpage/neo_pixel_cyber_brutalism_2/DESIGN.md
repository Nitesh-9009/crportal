---
name: Neo-Pixel Cyber-Brutalism
colors:
  surface: '#111319'
  surface-dim: '#111319'
  surface-bright: '#373940'
  surface-container-lowest: '#0c0e14'
  surface-container-low: '#191b22'
  surface-container: '#1e1f26'
  surface-container-high: '#282a30'
  surface-container-highest: '#33343b'
  on-surface: '#e2e2eb'
  on-surface-variant: '#d1c6ac'
  inverse-surface: '#e2e2eb'
  inverse-on-surface: '#2e3037'
  outline: '#9a9078'
  outline-variant: '#4e4633'
  surface-tint: '#efc10e'
  primary: '#fff0ce'
  on-primary: '#3c2f00'
  primary-container: '#ffd026'
  on-primary-container: '#705900'
  inverse-primary: '#735c00'
  secondary: '#ffffff'
  on-secondary: '#00382b'
  secondary-container: '#24ffcd'
  on-secondary-container: '#00725a'
  tertiary: '#c5ffcd'
  on-tertiary: '#003918'
  tertiary-container: '#2bf381'
  on-tertiary-container: '#006a33'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe087'
  primary-fixed-dim: '#efc10e'
  on-primary-fixed: '#231a00'
  on-primary-fixed-variant: '#574500'
  secondary-fixed: '#24ffcd'
  secondary-fixed-dim: '#00e0b3'
  on-secondary-fixed: '#002118'
  on-secondary-fixed-variant: '#00513f'
  tertiary-fixed: '#62ff96'
  tertiary-fixed-dim: '#00e475'
  on-tertiary-fixed: '#00210b'
  on-tertiary-fixed-variant: '#005226'
  background: '#111319'
  on-background: '#e2e2eb'
  surface-variant: '#33343b'
typography:
  display-lg:
    fontFamily: Space Mono
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.04em
  display-lg-mobile:
    fontFamily: Space Mono
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.03em
  headline-lg:
    fontFamily: Space Mono
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Space Mono
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Mono
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: 0em
  headline-sm:
    fontFamily: Space Mono
    fontSize: 20px
    fontWeight: '700'
    lineHeight: 28px
    letterSpacing: 0em
  body-lg:
    fontFamily: Space Mono
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: 0em
  body-md:
    fontFamily: Space Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
    letterSpacing: 0em
  body-sm:
    fontFamily: Space Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: 0.02em
  label-lg:
    fontFamily: Space Mono
    fontSize: 14px
    fontWeight: '700'
    lineHeight: 20px
    letterSpacing: 0.08em
  label-md:
    fontFamily: Space Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.06em
  label-sm:
    fontFamily: Space Mono
    fontSize: 10px
    fontWeight: '700'
    lineHeight: 14px
    letterSpacing: 0.1em
spacing:
  gutter: 1rem
  gutter-mobile: 0.5rem
  margin: 2rem
  margin-mobile: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system combines raw cyber-brutalist functionalism with retro 8-bit/16-bit arcade aesthetics, engineered specifically for high-intensity engineering campus operations and portal navigation. It captures the spirit of underground hacker consoles, terminal interfaces, and technical competitions.

The target audience comprises student coordinators, tech leads, and campus delegates who prize extreme informational clarity, direct keyboard-friendly ergonomics, and unapologetic visual identity. The experience rejects sanitized corporate minimalism in favor of unapologetic terminal aesthetics: hard angularity, visible pixel framing, intense neon contrast, mechanical tactile feedback, and relentless utility.

## Colors

The palette is anchored in an abyss of deep charcoals and obsidians, cut through by radioactive neons that evoke arcade CRTs and terminal phosphors:

- **Surface Base (`#0F1117`)**: Deep terminal ground; infinite abyss canvas for high contrast.
- **Surface Elevation 1 (`#161822`)**: Structural panels, containers, and table backdrops.
- **Surface Elevation 2 (`#1E2230`)**: Hover states, active data blocks, nested cards, and toolbars.
- **Primary Cyber Gold (`#FFD026` / `#FDB813`)**: Core brand accent, operational triggers, call-to-actions, and status indicators for primary tasks.
- **Secondary Cyber Cyan (`#00FFCC`)**: High-priority telemetry, secondary command pathways, active data cursors, and navigational pings.
- **Tertiary Matrix Green (`#00E676`)**: Verification tags, live sync states, terminal outputs, and system success notifications.
- **Border / Outline Grid (`#2B3245`)**: Structural panel grid boundaries.
- **Brutalist Shadow Tint (`#000000` / `#0A0B10`)**: Total-absorption drop shadows for hard elevation cuts.

## Typography

Typography prioritizes fixed-width precision and structural legibility. `Space Mono` governs all headings, tabular data, metrics, and narrative content to maintain a command-line feel. 

- **Display & Section Headers**: Rendered in uppercase `Space Mono` with negative letter-spacing to form cohesive, banner-like visual blocks.
- **Labels & Micro-Copy**: Emphasize uppercase tracking (`+0.06em` to `+0.1em`) to mimic raw firmware flags and console telemetry.
- **Numbers & Metrics**: Take advantage of monospace tabular figures to prevent jitter during real-time data refreshes.

## Layout & Spacing

The layout is built upon an uncompromising, rigid 12-column grid system calibrated around an 8px base module:

- **Desktop (1024px+)**: 12 columns, 16px (`1rem`) gutters, 32px (`2rem`) outer canvas margins. Multi-pane dashboard split with fixed terminal toolbars and flexible data canvases.
- **Tablet (768px - 1023px)**: 8 columns, 16px gutters, 24px margins. Sidebar panels collapse into high-contrast pixel tabs.
- **Mobile (< 768px)**: 4 columns, 8px (`0.5rem`) gutters, 16px (`1rem`) outer margins. Multi-column metric cards stack into singular vertical arrays.

Gaps and padding strictly conform to the 4px/8px pixel grid. Spacing is tight and utilitarian, maximizing information density without sacrificing touch targets or scanability.

## Elevation & Depth

Depth ignores soft natural lighting in favor of harsh mechanical hard-offsets and neon CRT backglow:

- **Hard Brutalist Drop Shadows**: Surfaces do not use blurry diffuse shadows. Elevation is achieved via solid `4px 4px 0px #000000` or `6px 6px 0px #000000` hard-edge steps.
- **Crisp Pixel Borders**: All structural components are encased in sharp 2px solid outlines (`#2B3245` base, `#FFD026` primary, or `#00FFCC` secondary).
- **Pixel Glowing Highlights**: Active, focused, or critical alerts combine the hard shadow with an intentional neon rim (`box-shadow: 4px 4px 0px #000000, 0 0 12px rgba(0, 255, 204, 0.4)`).
- **Stepped Stacking**: Overlays and modals project a hard `8px 8px 0px #000000` displacement with an underlying 80% opacity `#0F1117` scanline backdrop.

## Shapes

The geometric rule across the entire system is strictly **Level 0 (Sharp)**:
- Every corner has `border-radius: 0px`. Rounded geometry is forbidden.
- Chamfered cut corners (45-degree 6px pixel corner snips) are permitted solely for prominent action buttons, badge flags, and modal header containers via CSS clip-path or stepped border emulations.
- The silhouette reinforces modular hardware chassis, circuit boards, and pixelated displays.

## Components

### Buttons
- **Primary Cyber Button**: Background `#FFD026`, text `#0F1117`, border `2px solid #000000`, shadow `4px 4px 0px #000000`. Active state shifts the button `translate(2px, 2px)` with shadow reduced to `2px 2px 0px #000000`. Text uppercase `Space Mono` bold.
- **Secondary Ghost Button**: Background `#161822`, text `#00FFCC`, border `2px solid #00FFCC`, shadow `4px 4px 0px #000000`. Hover state triggers background `#00FFCC` with text `#0F1117`.
- **Destructive Action**: Background `#161822`, text `#FF3366`, border `2px solid #FF3366`, shadow `4px 4px 0px #000000`.

### Cards & Data Panels
- Built with background `#161822`, a `2px solid #2B3245` outline, and a `4px 4px 0px #000000` base shadow.
- Top bar of cards features an optional mechanical header strip (`#1E2230`) containing a monospace title, terminal status code (e.g., `// SEC_04`), and decorative pixel icons.

### Inputs & Select Fields
- Dark console entry: background `#0F1117`, text `#FFFFFF`, border `2px solid #2B3245`.
- Focus state updates the border to `2px solid #00FFCC` with a persistent blinking block cursor (`▋`) and an optional soft cyber glow (`0 0 8px rgba(0, 255, 204, 0.3)`).

### Chips & Status Badges
- Sharp rectangular capsules: 0px radius, uppercase `Space Mono` 10px bold text.
- Verified / Approved: `#00E676` border and text on `#0F1117` background with a leading green pixel block indicator.
- Pending / CR Action: `#FFD026` border and text on `#0F1117`.

### Checkboxes & Radios
- Checkbox: A 16x16px square, `2px solid #2B3245` border, background `#0F1117`. When checked, fills with `#FFD026` border and a solid interior sharp pixel check or cross (`#0F1117`).
- Radio Button: Rendered as a sharp diamond or square-within-square instead of traditional circular motifs.

### Portal-Specific Additions
- **Terminal Console Tray**: Bottom-anchored collapsible log stream rendering execution messages in `#00E676`.
- **Leaderboard / Task Matrix**: Tabular interface with zebra stripes using alternating `#161822` and `#1E2230` rows and solid `#000000` borders.