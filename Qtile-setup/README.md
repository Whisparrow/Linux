****Qtile Setup****

«A carefully crafted Qtile desktop environment built around simplicity, speed, and customization.»

This repository contains my personal Qtile configuration, supporting scripts, terminal setup, compositor configuration, and other resources that together create a lightweight yet feature-rich Linux desktop.
The goal of this project isn't to recreate a full desktop environment—it's to build one from carefully selected components that work well together while remaining fast, clean, and enjoyable to use.
Every configuration included here has been customized for my own workflow. If something looks unusual, there's probably a reason for it... or I was experimenting at 2 AM. Both are equally possible.

---

**Philosophy**

Desktop environments often come with everything pre-installed, whether you need it or not.
This setup takes a different approach.
Instead of installing a complete desktop environment and disabling features later, I prefer building the desktop piece by piece. Every component has a specific purpose, and every configuration exists because it improves my workflow.

The result is a desktop that is:

- Lightweight
- Keyboard driven
- Highly customizable
- Easy to maintain
- Modular
- Pleasant to use every day

Rather than relying on one large application to do everything, this setup combines smaller tools that each excel at their specific job.
- Qtile manages the windows.
- Picom provides modern compositing effects.
- Rofi launches applications and powers several custom menus.
- Kitty handles terminal duties.
- Fish makes the terminal a little friendlier.
- The rest is held together with Python, shell scripts, and probably too much coffee.

---

**Features**

Current highlights of this configuration include:

- Fully customized Qtile configuration
- Gruvbox-inspired color palette
- Custom status bar with useful system information
- Dedicated Picom configuration
- Rounded window corners
- Window shadows and smooth fading animations
- Hardware media key support
- Brightness controls
- Volume controls
- Lock screen shortcut
- Custom power menu
- GNOME-style window switcher built with Rofi
- Clipboard history manager powered by Xclip and Rofi
- XFCE notification daemon integration
- XFCE screensaver integration
- Automatic wallpaper loading
- Startup automation
- Modular configuration layout
- Kitty terminal configuration
- Fish shell configuration
- Ready for future expansion

*This project will continue evolving as new features and improvements are added.*

---

**Screenshots**

<table>
  <tr>
    <td><a href="https://github.com/user-attachments/assets/4c114bd9-d5cf-4f4d-93da-a22fb9e3adf1"><img src="https://github.com/user-attachments/assets/4c114bd9-d5cf-4f4d-93da-a22fb9e3adf1" width="400"></a></td>
    <td><a href="https://github.com/user-attachments/assets/0fcd03a6-7547-4ea7-bb0c-dc1ca090004a"><img src="https://github.com/user-attachments/assets/0fcd03a6-7547-4ea7-bb0c-dc1ca090004a" width="400"></a></td>
  </tr>
  <tr>
    <td><a href="https://github.com/user-attachments/assets/f98915fb-dfee-4b9b-8450-f34ce3b40cf1"><img src="https://github.com/user-attachments/assets/f98915fb-dfee-4b9b-8450-f34ce3b40cf1" width="400"></a></td>
    <td><a href="https://github.com/user-attachments/assets/b3578b39-931c-4c45-963a-c730fa14ebfc"><img src="https://github.com/user-attachments/assets/b3578b39-931c-4c45-963a-c730fa14ebfc" width="400"></a></td>
  </tr>
  <tr>
    <td colspan="2" align="center"><a href="https://github.com/user-attachments/assets/1229ebe4-16f9-477f-a716-cc96c2f25f8a"><img src="https://github.com/user-attachments/assets/1229ebe4-16f9-477f-a716-cc96c2f25f8a" width="400"></a></td>
  </tr>
</table>


---

**Repository Structure:**

The repository is organized so each component remains independent and easy to maintain.
<img width="156" height="179" alt="structure" src="https://github.com/user-attachments/assets/12d07d78-9100-4b71-9ee8-040bb95ef564" />

As the project grows, additional configuration files and supporting resources may be added without changing the overall structure.

---

**Required Packages:**

The following applications are used throughout this setup.
<img width="439" height="226" alt="image" src="https://github.com/user-attachments/assets/3e3250f2-77ee-4205-bbb4-ce489ffbe57b" />


**Optional:**

This setup uses "powerprofilesctl" to switch between power profiles.
If your system does not support Power Profiles Daemon, simply skip this dependency. Everything else will continue working normally.

---

**Recommended Tools:**

*Kitty*

This configuration is designed around Kitty as the primary terminal emulator.
It is fast, GPU accelerated, highly configurable, and simply a pleasure to use.

Could another terminal work?
Absolutely.

Will I still recommend Kitty?
Also absolutely.

---

*Fish Shell*

Fish is my preferred interactive shell.
It provides sensible defaults, excellent command completion, syntax highlighting, and a much nicer command-line experience without extensive manual configuration.
You are free to continue using Bash or Zsh if you prefer, but the included Kitty configuration assumes Fish is available.

---

*Wallpapers*

A desktop isn't complete without a good wallpaper.
This repository also includes a curated collection of wallpapers that I personally use and recommend.
Feel free to use them, mix them into your own setup, or simply browse through them until you inevitably spend twenty minutes choosing one.
We've all been there.

---

**Installation**

Getting this setup running is straightforward. Install the required packages, copy the configuration files into the appropriate directories, restart Qtile, and you're ready to go.

«Note
This setup is currently designed for X11. While Qtile also supports Wayland, this configuration has been developed and tested primarily on the X11 backend.»

---
**Install Dependencies:**

Below is a list of the primary applications used throughout this configuration.

*Qtile*

The heart of this project.
Qtile is a highly configurable tiling window manager written entirely in Python. If you enjoy configuring your desktop using actual programming instead of XML files, you're in the right place.

*Feh*

Used for wallpaper management.
On startup, Feh restores the wallpaper automatically through the autostart script.
Without it, you'll probably end up staring at a solid-colored background.
Which... is technically minimalist.

*Rofi*

Rofi is used for much more than launching applications.
Within this setup it powers:
- Application launcher
- Custom power menu
- Clipboard history selector
- GNOME-style window switcher

It's one of those utilities that quietly becomes indispensable.

*Picom*

Picom is responsible for desktop compositing.
It provides:
- Rounded corners
- Window shadows
- Smooth fade animations
- Transparency support
- Better visual polish

Could you run Qtile without Picom?
Absolutely.
Should you?
...because why not?

*Flameshot*

Flameshot handles screenshots.
Simply press the configured Print Screen shortcut and capture exactly what you need.
No complicated menus.

*Xclip*

This setup includes a lightweight clipboard history system built around Xclip.
The clipboard is continuously monitored in the background and can later be searched using Rofi.
It may not be the fanciest clipboard manager ever written.
But it works.


*Power Profiles Daemon* **(Optional)**

My setup includes support for:
-Balanced
-Performance
-Power Saver
using powerprofilesctl.

If your distribution does not provide this utility—or you simply don't use power profiles—you can safely skip this dependency.
The remainder of the configuration will continue to function normally.

---

**Recommended Applications**
These aren't strictly required, but the configuration is designed around them.

*Kitty*

Kitty is the terminal emulator used throughout this project.
Features include:
- GPU accelerated rendering
- Transparency
- Excellent font rendering
- Fast startup
- Extensive customization

The included Kitty configuration will be available inside this repository.
If you prefer another terminal emulator, simply update the "terminal" variable inside "config.py".


*Fish*

Fish is my preferred interactive shell.
It provides:
- Smart autosuggestions
- Syntax highlighting
- Better tab completion
- Cleaner default experience

No massive shell configuration required.
It simply works.


---

**Wallpapers**

The repository includes a collection of wallpapers that I personally use throughout my setup.
Feel free to use them directly or replace them with your own favorites.
The autostart script expects a wallpaper to be available, so remember to update the wallpaper path if you choose a different image.

---

**First Startup**

After copying the configuration files:

1. Restart Qtile.
2. Verify that Picom starts automatically.
3. Confirm the wallpaper loads correctly.
4. Open Kitty.
5. Launch Rofi.
6. Test the clipboard manager.
7. Smile when everything works on the first attempt.

If it doesn't...

Welcome to Linux.

---

**Future additions may include:**

- Themes
- Fonts
- Additional scripts
- Widget modules
- Alternative layouts
- Documentation
- Screenshots
- Extras

The goal is to keep everything organized, modular, and easy to maintain.

---

**Configuration Breakdown**

This repository is intentionally modular.
Rather than placing every setting into a single configuration file, responsibilities are divided across dedicated files and directories. This makes the setup easier to understand, maintain, and customize over time.
Each component has a specific purpose, and together they form the complete desktop experience.

---

**"config.py"**

The heart of the entire setup.
This file defines how Qtile behaves, how windows are managed, how applications are launched, and how the desktop responds to keyboard shortcuts.

Highlights include:
- Custom keybindings
- Workspace (Group) management
- Window layouts
- Status bar configuration
- Widgets
- Floating window rules
- Startup hooks
- Mouse behavior
- Window management
- Application launcher integration

The configuration is written entirely in Python, allowing far more flexibility than traditional declarative configuration formats.
If you're comfortable writing Python, modifying Qtile quickly becomes second nature.

---

**Color Palette**

This setup uses a customized Gruvbox-inspired color palette.
The objective is simple:

- Comfortable during long coding sessions.
- High contrast without being overwhelming.
- Consistent colors across applications.
- Easy on the eyes during late-night debugging sessions.

Because let's be honest...
Most configuration happens after sunset.

---

**Keybindings**

Most daily tasks can be completed without touching the mouse.
Current shortcuts include support for:

## Applications
| Shortcut | Action |
|----------|--------|
| Mod + Enter | Open terminal |
| Mod + d | Launch application launcher |
| Mod + b | Open browser |

## Windows
| Shortcut | Action |
|----------|--------|
| Mod + q | Close focused window |
| Mod + Space | Toggle floating |
| Mod + f | Toggle fullscreen |
| Mod + t | Toggle the focused window between tiled and floating mode |

## Layouts
| Shortcut | Action |
|----------|--------|
| Mod + Tab | Open the GNOME-style application switcher (includes minimized windows) |
| Mod + h | Focus left |
| Mod + l | Focus right |

## Scratchpads
| Shortcut | Action |
|----------|--------|
| Mod + n | Toggle notes |

## Workspaces
| Shortcut | Action |
|----------|--------|
| Mod + 1–9 | Switch workspace |
| Mod + Shift + 1–9 | Move window to workspace |



The goal is to keep the desktop fast, efficient, and keyboard-first without making the shortcuts difficult to remember.

---

**Status Bar**

The top bar provides useful system information without becoming cluttered.
Current widgets include:

- Workspaces
- Current layout
- Active window title
- Network traffic
- CPU usage
- Memory usage
- Audio volume
- Battery status
- Bluetooth device
- Wi-Fi network
- Date & time

Everything is designed to be informative while remaining lightweight.

---

**Autostart**

The "autostart.sh" script is executed automatically whenever Qtile starts.
Instead of manually launching background services after every login, the desktop configures itself automatically.
Current startup tasks include:

- Setting the desktop wallpaper using Feh
- Starting Picom
- Launching the Polkit authentication agent
- Starting the XFCE notification daemon
- Starting the XFCE screensaver
- Enabling automatic screen locking
- Setting the default power profile
- Initializing clipboard history
- Cleaning temporary clipboard data

Once configured, login becomes as simple as logging in.
Exactly how it should be.

---

**Clipboard History**

One of my favorite additions to this setup.
Instead of relying on a dedicated clipboard manager, this configuration implements a lightweight clipboard history system using:
- Xclip
- Shell scripting
- Rofi

The clipboard is monitored in the background, duplicate entries are removed automatically, and the most recent items remain easily searchable through a simple Rofi interface.
Minimal dependencies.
Minimal resource usage.
Maximum convenience.

---

**GNOME-style Window Switcher**

Qtile doesn't normally include a window switcher that behaves like GNOME.
So...
I built one.
Using Python and Rofi, this configuration provides a clean window selection interface that displays open windows, identifies minimized applications, and restores them when selected.
It feels familiar while remaining fully integrated into Qtile.

---

**Picom Configuration**

Desktop compositing is handled by a dedicated Picom configuration.
Features include:

- Rounded corners
- Window shadows
- Smooth fade animations
- Transparency support
- GLX backend
- VSync enabled
- Optimized rendering
- Sensible default rules

The aim isn't excessive eye candy.
Just enough polish to make the desktop feel modern without sacrificing performance.

---

**Kitty Configuration**

Kitty serves as the default terminal emulator throughout this setup.
The included configuration focuses on usability rather than unnecessary complexity.
Highlights include:

- Gruvbox theme
- Fish as the default shell
- Semi-transparent background
- Comfortable window padding
- Cursor customization
- Font scaling shortcuts
- Cleaner window appearance
- Simplified key mappings

The terminal is where many Linux users spend a significant amount of time.
It should feel comfortable.

---

**Scripts**

The "scripts/" directory contains small utilities that extend the desktop beyond Qtile's built-in functionality.
Examples include:

- Power menu
- Power profile selector
- Automation helpers
- Utility scripts

Each script is designed to perform one task well and integrate naturally with the rest of the desktop.
As the project grows, this directory will continue expanding with additional tools and workflow improvements.


---

**Customization**

This setup is meant to be customized.

Some ideas include:
- Replace the color scheme.
- Modify keybindings.
- Add widgets.
- Change layouts.
- Swap terminal emulators.
- Replace Rofi themes.
- Configure different wallpapers.
- Expand the scripts directory.

If something doesn't fit your workflow, change it.
That's one of the best parts of Linux.
Make the desktop yours.

---

**Credits**

This setup wouldn't exist without the amazing open-source community.
A huge thanks to:
- The Qtile developers for creating such a powerful and flexible window manager.
- Everyone who shares their configurations, scripts, and ideas online.
- The Linux community for making customization and learning so accessible.
Many ideas were inspired by countless GitHub repositories, Reddit discussions, and community forums. While this configuration was built and organized by me, it stands on the shoulders of an incredible community.

---

**Reporting Issues**

If you encounter a bug or something doesn't work as expected:

- Open an issue describing the problem.
- Include your Linux distribution.
- Include any error messages or logs if possible.
- Mention the steps needed to reproduce the issue.

The more information you provide, the easier it is to identify and fix the problem.

---

**Suggestions**

Have an idea that could improve this configuration?
Feel free to open an issue or submit a pull request.
Whether it's a bug fix, a new feature, better documentation, or a small quality-of-life improvement, contributions are always appreciated.

---

***If You Like This Project***

If this configuration helped you or inspired your own setup:

- ⭐ Star the repository.
- 🍴 Fork it and make it your own.
- 📢 Share it with others who enjoy Linux customization.

It really helps motivate future improvements.

---

**License**

This project is released under the MIT License unless stated otherwise.
You're free to use, modify, and distribute it according to the terms of the license.

---

**Final Words**

Thank you for checking out my Qtile setup.
This repository started as my personal desktop configuration and gradually evolved into something I wanted to share with others. I hope it saves you time, gives you ideas, or simply inspires you to explore what Qtile and Linux customization have to offer.
If you're new to Qtile, don't worry if everything doesn't make sense right away. Take your time, experiment, read the configuration, and don't be afraid to break things—you'll learn a lot by fixing them.
Most importantly, have fun customizing your desktop. That's what this project is all about.

Happy ricing! 🚀
