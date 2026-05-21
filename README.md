# Shooter Game

A 2D space shooter built with Python + Pygame. Asteroids-style tank controls, facing-direction fire, and screen wrap. Clean modular architecture designed to grow through three build phases.

---

## Controls

| Key | Action |
|-----|--------|
| `W` | Thrust forward |
| `A` | Rotate left |
| `D` | Rotate right |
| `Space` | Fire |
| `Esc` | Quit |

---

## Project Structure

```
shooter-game/
├── main.py              # Entry point
├── game.py              # Game class + main loop
├── settings.py          # All tunable constants (speed, FPS, colors, etc.)
├── core/
│   ├── clock.py         # FPS cap
│   ├── input_handler.py # Keyboard + quit events
│   └── renderer.py      # All draw calls
├── entities/
│   ├── base_entity.py   # Sprite base class (position, velocity)
│   ├── player.py        # Movement, rotation, firing
│   └── bullet.py        # Velocity, lifetime, screen wrap
└── assets/              # Sprites and sounds (Phase 3)
```

---

## Getting Started

**Requirements:** Python 3.10+ and Pygame 2.x

```bash
pip install pygame
python main.py
```

---

## Build Phases

- [x] **Phase 1** — Player ship with tank controls and rotation
- [x] **Phase 2** — Bullet firing with velocity, lifetime culling, screen wrap
- [ ] **Phase 3** — Enemies, collision detection, sound

---

## Tuning

All gameplay constants live in [`settings.py`](settings.py) — no digging through logic files to tweak feel.

| Constant | Default | Effect |
|----------|---------|--------|
| `PLAYER_SPEED` | `4` | Thrust force per frame |
| `ROTATE_SPEED` | `4` | Degrees rotated per frame |
| `FRICTION` | `0.97` | Velocity decay (1.0 = no friction) |
| `BULLET_SPEED` | `10` | Muzzle velocity added to player velocity |
| `BULLET_LIFETIME` | `60` | Frames before bullet is removed |
