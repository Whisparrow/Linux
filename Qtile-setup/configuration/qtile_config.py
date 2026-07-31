import os
from collections.abc import Callable

import libqtile.resources
from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Output, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "kitty"

# Gruvbox Dark Palette (Medium Contrast)
gruvbox = {
    'bg':          '#282828', # Dark background
    'fg':          '#ebdbb2', # Light foreground
    'bg0_h':       '#1d2021', # Hard contrast background
    'bg1':         '#3c3836', # Lighter background (used for inactive tabs)
    'bg2':         '#504945',
    'bg3':         '#665c54',
    'bg4':         '#7c6f64',
    'gray':        '#928374',
    'red':         '#cc241d',
    'green':       '#98971a',
    'yellow':      '#d79921',
    'blue':        '#458588',
    'purple':      '#b16286',
    'aqua':        '#689d6a',
    'orange':      '#d65d0e',
    'fg4':         '#a89984',
    'bright_red':  '#fb4934',
    'bright_green':'#b8bb26',
    'bright_yellow':'#fabd2f',
    'bright_blue': '#83a598',
    'bright_purple':'#d3869b',
    'bright_aqua': '#8ec07c',
    'bright_orange':'#fe8019'
}

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.spawn("rofi -show drun"), desc="Launch Rofi"),
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Take a screenshot with Flameshot"),
    Key([mod, "control"], "v", lazy.spawn("bash -c 'chosen=$(tac ~/.clipboard_history | rofi -dmenu -p \"Clipboard:\"); if [ ! -z \"$chosen\" ]; then echo -n \"$chosen\" | xclip -selection clipboard; fi'"), desc="Open Clipboard History via Rofi"),
    Key(["shift", "control"], "Return", lazy.spawn("/home/aster/.config/qtile/scripts/powerprofile_menu.sh"), desc="Power profile menu"),
    Key([mod], "l", lazy.spawn("xfce4-screensaver-command --lock"), desc="Lock screen"),
    # Move windows betoween left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window to the upwards"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window to the downwards"),
    Key([mod, "control"], "n", lazy.layout.normalize(), desc="Reset window sizes back to default"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='playerctl'),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='playerctl'),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc='playerctl'),
    Key([], "XF86AudioMicMute", lazy.spawn("pactl set-source-mute @DEFAULT_SOURCE@ toggle"), desc="Mic mute"),
    Key(["mod1"], "F4", lazy.spawn("/home/aster/.config/qtile/scripts/power_menu.sh"), desc="Power menu"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
     ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key(["shift"], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    
]
 # =====================================================================
# GNOME-STYLE ROFI WINDOW SWITCHER ENGINE (PASTED SAFELY OUTSIDE THE LIST)
# =====================================================================
import subprocess
import threading
from libqtile.lazy import lazy

def _run_rofi_async(qtile, win_list, win_map):
    try:
        rofi_input = "\n".join(win_list)
        proc = subprocess.Popen(
            ["rofi", "-dmenu", "-i", "-p", "Windows"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True
        )
        stdout, _ = proc.communicate(input=rofi_input)
        selected = stdout.strip()

        if selected in win_map:
            window_id = win_map[selected]
            qtile.call_soon(_restore_window, qtile, window_id)
    except Exception:
        pass

def _restore_window(qtile, window_id):
    for w in qtile.current_group.windows:
        if id(w) == window_id:
            if w.minimized:
                w.toggle_minimize()
            qtile.current_group.focus(w)
            break

@lazy.function
def gnome_style_switcher(qtile):
    windows = qtile.current_group.windows
    if not windows:
        return

    win_list = []
    win_map = {}
    for w in windows:
        if w.name:
            state = " [Minimized]" if w.minimized else ""
            display_name = f"{w.name}{state}"
            win_list.append(display_name)
            win_map[display_name] = id(w)

    threading.Thread(target=_run_rofi_async, args=(qtile, win_list, win_map), daemon=True).start()

# =====================================================================
# APPENDING THE SWITCHER AND THE REST OF YOUR KEYBINDINGS
# =====================================================================

keys.append(
    Key([mod], "Tab", gnome_style_switcher(), desc="Gnome-style window switcher")
)


keys.extend([
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window"

),
      
    Key([mod], "h", lazy.window.toggle_minimize(), desc="Toggle minimize on focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "Escape", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
])
# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layout_theme = {
    "border_width": 2,
    "margin": 5,
    "border_focus": "FFFFFF",
    "border_normal": "CCCCCC"
}

layouts = [
    layout.Bsp(**layout_theme),
    # layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Columns(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.MonadTall(**layout_theme),
    # layout.MonadWide(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(**layout_theme),
    # layout.TreeTab(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Zoomy(**layout_theme),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

logo = os.path.join(os.path.dirname(libqtile.resources.__file__), "logo.png")
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    fontsize=10,
                    margin_y=5,
                    margin_x=10,
                    padding_y=0,
                    padding_x=2,
                    borderwidth=3,
                    active="#FFFFFF",
                    inactive="#777777",
                    rounded=False,
                    highlight_method="line",
                    this_current_screen_border="#d75f5f",
                ),
                widget.TextBox(text="|", padding=2, fontsize=14),
                widget.CurrentLayout(padding=5),
                widget.TextBox(text="|", padding=2, fontsize=14),
                widget.WindowName(padding=8, max_chars=40),
                widget.Spacer(),
                widget.Net(format="Net: {down} ↓ {up} ↑", padding=8),
                widget.CPU(format="Cpu: {load_percent}%", padding=8),
                widget.Memory(format="{MemUsed: .0f}{mm}", fmt="Mem: {}", padding=8),
                widget.Volume(fmt="Vol: {}", padding=8),
                widget.Battery(format="Juice:{percent:2.0%}", padding=8),
                widget.GenPollText(
    update_interval=5,
    func=lambda: subprocess.check_output(
        "bluetoothctl info | grep Name | awk '{print $2}'",
        shell=True
    ).decode().strip(),
    padding=8,
),
                widget.Wlan(interface="wlan0", format="{essid}", disconnected_message="N/A", padding=8),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p", padding=8),
#               widget.Systray(padding=6),
            ],
            26,
            background="#00000000",
        ),
    ),
]

# Instead of screens, you can define a function here to specify which Screen
# should correspond to which Output.
fake_screens: list[Screen] | None = None

# Instead of screens or fake screens, you can define a function here that
# returns a list of Screen objects based on the list of Outputs; that way you
# can decide based on e.g. the number of screens, or which ports are plugged
# in exactly what do render in each bar for each screen.
generate_screens: Callable[[list[Output]], list[Screen]] | None = None

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    **layout_theme,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="gnome-calculator"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
focus_previous_on_window_remove = False
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

idle_timers = []  # type: list
idle_inhibitors = []  # type: list

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

import os
import subprocess
from libqtile import hook

@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([script])
