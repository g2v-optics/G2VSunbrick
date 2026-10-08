# Sunbrick One-Click Sun (Windows Offline Kit)

One-Click Sun is G2V Optics' control software for the Sunbrick solar simulator. Pick a place and a time, and the Sunbrick reproduces the sunlight you would see there.

This kit installs everything you need on a Windows laptop **without an internet connection**.

## Features

- **Realistic sunlight for any place on Earth.** The software works out where the sun is for your chosen location and time, from the North Pole to the South Pole.
- **Day and night map.** A world map shows which parts of the Earth are in daylight, with a realistic sunrise and sunset line.
- **Matches the sunlight spectrum.** The Sunbrick's light is adjusted to match the sun's spectrum for the conditions, from direct sunlight in space (air mass 0) to a sun very low on the horizon (air mass 40).
- **Accounts for altitude.** Elevation at your location is taken into account.
- **Simple controls.** The software drives the Sunbrick over a single USB connection.
- **Built-in test mode.** A Diagnostics mode lets you check the installation before you connect the Sunbrick.

## System Requirements

- A 64-bit Windows laptop or PC
- Administrator rights on the computer (needed once, for the installation)
- A USB connection to your Sunbrick
- The calibration files for your Sunbrick (see Installation, step 5)

You do not need to install Python or anything else beforehand. The kit includes it.

## Installation

1. **Unzip the kit.** Right-click the `.zip` file you downloaded, choose **Extract All**, and pick any folder.
2. **Run the installer.** Open the extracted folder, right-click `Install-Sunbrick.cmd`, and choose **Run as administrator**. Wait until it finishes. It installs the software and adds **One-Click Sun** shortcuts.
3. **Test the installation (optional).** Open **One-Click Sun (Diagnostics)** from the Start menu. It uses a simulated Sunbrick, so you can confirm the software works before connecting anything.
4. **Connect your Sunbrick.** Plug it in over USB, then start **One-Click Sun** from the desktop.
5. **Install your calibration (first launch only).**
   - The software tells you no calibration is installed and opens a file window.
   - Browse to the calibration files for your Sunbrick. They are in the `AM0` and `AM1.5G` folders that came with your unit.
   - Select any one `.spectrum` file, for example `AM1.5G\am1.5g-1.0.data.spectrum`.
   - The software finds the rest of the files, asks you to confirm the folder, then sets everything up and starts.
   - You only do this once. Later launches start straight away.

> **Use the calibration files from your own Sunbrick.** The software cannot tell which unit a calibration belongs to. Files from a different Sunbrick will install without any warning but will produce the wrong light. Check the serial number on your Sunbrick's label against the folder you selected before you confirm.

**If the calibration files are rejected**, nothing is installed and the software lists what is wrong so you can choose again. Common causes are a missing `AM0` file, fewer than two `AM1.5G` files, two files for the same intensity, or files that belong to a different Sunbrick model.

## Usage

- **Start the software:** double-click **One-Click Sun** on the desktop with your Sunbrick connected.
- **Practice without hardware:** open **One-Click Sun (Diagnostics)** from the Start menu. This runs against a simulated Sunbrick.
- **Change the location or time:** set these in the software. The map and the Sunbrick's light update to match.

## Need help?

Contact G2V Optics and include the serial number on your Sunbrick's label. If the installer fails, the installation log is saved in `C:\ProgramData\G2V\OneClickSun\logs\`. Please send us the latest file in that folder.
