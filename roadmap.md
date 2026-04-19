# Bitty Music Archivist Roadmap

## Vision

Bitty Music Archivist is a personal Python side project for organizing and renaming a local music library safely and flexibly.

The long-term goal is to grow it from a simple file renamer into a lightweight archival tool with configurable rules, duplicate handling, and a themed interface.

---

## Core Priorities

- Safe file operations
- Clear rename and organization logic
- Useful metadata handling
- Gradual expansion without overcomplicating the project too early

---

## System Features (Overview)

### Renaming

- Basic renamer:
    - Replaces "_" with " "
- Metadata-based renamer:
    - v1 Format: 'Title - Artist.mp3'
    - v2 Allow user to choose meta-data fields for naming convention and save user preference.
    - v3 Detect similar or conflicting meta-data and prompt user for values and save user preference.

---

### Organization

- Organize files into folders based on meta-data
    - v1 Will organize music files into folders created according to meta-data 'Artist'
    - v2 Allow user to choose meta-data fields for archive organization and save user preference.
    - v3 Detect similar or conflicting artists from multiple data fields and will prompt user and allow custom values for save folders for user preference.

---

### User Interface (GUI)

- Add a tkinter GUI for user input
    - v1 Basic prompts, displays, organization and actions (renaming, organizing files in folders)
    - v2 Begins to save user preferences; when new files are added to archive, preferences are auto applied
    - v3 Begins to allow custom user preferences to naming and organization conventions

---

### Safety Features

- Dry-run mode enabled by default, but a setting possible to edit in UI via checkbox.
- Preview changes before execution, list the number of changes, have a detailed summary. Make a setting that allows user to select how detailed the preview is.
- Require user confirmation
- Generate operation history for undo. Operation history should be saved as a player inventory that can be used to revert titles and organization.
- Backup option before modifying files, allows save files of your archive, designating space available from computer.
- Undo capability using operation history/logs

---

### Metadata Handling

- Expand metadata selection and organization rules

---

### Archivist System (Ambitious / Future)

- Archivist system:
  - Create a snapshot of a music library
  - Compare new files against existing archive
  - Apply user-defined naming and organization rules automatically
  - Prompt user for edge or ambiguous cases

- Duplicate detection (same audio, different files)
- Compatibility with Musicolet mobile app
- Themed UI (e.g., retro archive aesthetic)

---

## Stage 1: Initial Release

Focus: build the minimum working version and verify the core workflow.

### Goals

- Build and test a basic renamer that replaces `_` with spaces
- Build and test a metadata-based renamer
- Add dry-run preview
- Add backup and undo capability
- Build a basic organizer using metadata
- Add a tkinter GUI for user input
- Expand metadata selection and organization rules

### Expected Outcome

A functional personal-use tool that can safely rename and organize music files with a simple interface.

---

### Anticipated Stage 1 Structure
bitty_music_archivist/
├── app.py
├── basic.py
├── metadata_renamer.py
├── organizer.py
├── file_ops.py
├── docs/
├── logs/
├── test_music/
├── requirements.txt
└── README.md


---

## Stage 2: Development Plan ("Useful Release")

Focus: make the tool **reliable, interactive, and user-configurable**

- Implement full safety system:
  - dry-run → preview → confirm → execute → log
- Add metadata comparison and conflict detection
- Build user prompts for ambiguous naming/organization
- Save user decisions as reusable preferences
- Introduce structured modules (renamers, organizers, metadata, core)
- Add basic testing framework (pytest)
- Improve GUI with:
  - preview panel
  - confirmation dialogs
  - error handling feedback

---

### Anticipated Structure: Stage 2
music_archivist/
├── app.py
├── requirements.txt
├── README.md
├── logs/
├── test_music/
├── tests/
├── gui/
│ ├── main_window.py
│ ├── preview_panel.py
│ └── dialogs.py
├── renamers/
│ ├── basic.py
│ └── metadata.py
├── organizers/
│ └── organizer.py
├── metadata/
│ ├── reader.py
│ ├── normalizer.py
│ └── matcher.py
├── core/
│ ├── file_ops.py
│ ├── history.py
│ └── scanner.py
└── assets/


---

## Stage 3: Development Plan ("Archivist / Advanced")

Focus: turn tool into a **persistent, intelligent archive system**

- Implement user configuration system:
  - saved naming rules
  - saved folder structures
- Build archive snapshot system:
  - record state of library
  - compare against new files
- Add duplicate detection:
  - metadata + optional audio fingerprinting
- Build import pipeline:
  - process new files using saved rules
- Improve handling of edge cases:
  - partial metadata
  - conflicting artist names
- Expand UI:
  - archive view
  - conflict resolution UI
- Add optional theming and visual polish

---

### Anticipated Structure: Stage 3
music_archivist/
├── app.py
├── requirements.txt
├── README.md
├── logs/
├── test_music/
├── tests/
├── gui/
├── renamers/
├── organizers/
├── metadata/
├── core/
├── config/
│ ├── user_profiles.py
│ └── naming_rules.py
├── archivist/
│ ├── snapshot.py
│ ├── comparer.py
│ └── importer.py
└── assets/

---

## Dependencies

### Initial Release
- mutagen (metadata reading)

### Useful Release
- pytest (testing)
- pathvalidate (safe filenames)

### Ambitious Release
- rapidfuzz (fuzzy matching)
- send2trash (safe deletion)
- platformdirs (config/log locations)
- Pillow (UI images/icons)
- optional additional UI or utility libraries

---

## Packaging

Example build command:
pyinstaller --onefile --windowed --name "Music Archivist" app.py


---

## Notes

This roadmap is a planning document and may evolve as development progresses and practical needs become clearer.