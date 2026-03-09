# Nano Image Generator Skill

[简体中文](./README_CN.md)

A Claude Code skill for generating images using Gemini 3 Pro Preview (Nano Banana Pro).

## Features

- **Text-to-image generation** - Describe what you want, get an image
- **Reference image support** - Style transfer, character consistency (up to 14 images)
- **Multiple aspect ratios** - Square, portrait, landscape, cinematic
- **Resolution options** - 1K, 2K, 4K output

## Differences from [livelabs-ventures/nano-skills](https://github.com/livelabs-ventures/nano-skills)

| Feature | Original | This Version |
|---------|----------|--------------|
| Reference images | ❌ Not supported | ✅ Up to 14 images |
| API key config | Environment variable | Environment variable |

## Setup

### 1. Get Gemini API Key

Visit: https://aistudio.google.com/apikey

### 2. Configure API Key

Set the environment variable (do **not** hardcode the key in source files):

```bash
export GEMINI_API_KEY="AIzaSy..."
```

Add it to your shell profile (`~/.bashrc`, `~/.zshrc`) to persist:

```bash
echo 'export GEMINI_API_KEY="AIzaSy..."' >> ~/.zshrc
```

## Installation

### From Local Path

```bash
git clone https://github.com/YOUR_USERNAME/nano-image-generator-skill.git
```

Add to your `~/.claude/settings.json`:

```json
{
  "skills": [
    "/path/to/nano-image-generator-skill"
  ]
}
```

### From GitHub

```bash
claude skill add github:YOUR_USERNAME/nano-image-generator-skill
```

## Plugin Structure

```
nano-image-generator-skill/
├── SKILL.md                    # Skill definition for Claude Code
├── README.md                   # This file
├── README_CN.md                # Chinese documentation
└── scripts/
    └── generate_image.py       # Image generation script
```

## Usage

Once installed, Claude Code will automatically use this skill when you ask to:

- "Generate an image of..."
- "Create an icon for..."
- "Design a logo..."
- "Make a banner..."
- "Same style as this image..."

## Direct Script Usage

### Basic

```bash
python scripts/generate_image.py "A cute robot mascot" --output ./robot.png
```

### With Aspect Ratio

```bash
python scripts/generate_image.py "Website banner" --aspect 16:9 --output ./banner.png
```

### With Reference Image

```bash
python scripts/generate_image.py "Same character in a forest" --ref ./character.png --output ./forest.png
```

### Multiple References

```bash
python scripts/generate_image.py "Combine styles" --ref ./img1.png --ref ./img2.png --output ./combined.png
```

## Options

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `--aspect`, `-a` | `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9` | `1:1` | Aspect ratio |
| `--size`, `-s` | `1K`, `2K`, `4K` | `2K` | Resolution |
| `--ref`, `-r` | Image path | - | Reference image (repeatable, max 14) |

## License

MIT
