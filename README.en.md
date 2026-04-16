# Federal Republic of Soul - Archive

## Nature of this Archive
- This repository is merely a **personal cloud storage space** (it cannot be considered a "project"). It is used to store static setting files for the fictional country "Federal Republic of Soul", born from the **author's wild imagination and whimsical ideas**.
- It serves strictly as a personal auxiliary backup and sealed record for worldbuilding. There is no intention to build an active community or provide subsequent maintenance or releases, **let alone use it for commercial purposes or any copyright infringement activities**.

### Source Inspirations & Integration Framework (including but not limited to)
| Domain | Primary Source IP | Examples of Amalgamation |
| :--- | :--- | :--- |
| **Core Framework** | *Soul Land* Series | State name, Soul Guidance technology, Shrek Academy, etc. |
| **Elemental System** | *Genshin Impact* | Teyvat State, Elemental energy applications, Seven Nations structure, etc. |
| **Originium Tech** | *Arknights* | Arknights State, Originium Arts, Mobile City infrastructure, etc. |
| **Magic Admin** | *Harry Potter* Series | Ministry of Magic (Central Govt.), Hogwarts Department of Magic, etc. |
| **Space Tech** | *Honkai: Star Rail* | Cloud Knight military divisions, Orbital/Space station nomenclature, etc. |
| **Urban Legends** | *Touhou Project* Series | Gensokyo, Spell Card peacekeeping regulations |

**Typical Amalgamation Cases**:
- **Fatui Shrine**: Designated as a historical and cultural monument, occasionally serving as a special tribunal.
- **Ministry of Magic**: A core department under the Imperial Executive Yuan, featuring various localized sub-departments to vertically manage and regulate distinct magic systems from different cultural backgrounds.

## Note on Terminology and Translation

The selection of all nouns (including both Chinese and English terminology) within this setting serves the **overall atmosphere of this unique amalgamated world and the author's personal preferences**.

1.  **Author's Prerogative**: Whether a term retains its original English name, adopts a common translation, or is completely renamed, the **final criterion depends solely on the author's judgment**. The goal is to make it fit the context and style of this archive, as well as the author's personal taste.
2.  **Lore First**: All chosen Chinese and English forms of these terms should be regarded as the **official names** within this setting framework. Together, they constitute the identity elements of this fictional nation.
3.  **No "Standard" Answer**: There is no "uniquely correct" translation here; there are only names "used as such within this setting".

**Example**: In this setting, the official English name for "史莱克城" is **"Shrek City"**, and the official Chinese name for "Endfield State" is **"未央州"**. These are established lore facts, not translation conclusions, regardless of what the original English or Chinese names of these elements were in their source materials.

## Repository Structure
```text
Federal_Republic_of_Soul/ (Repository Root)
├── docs/                                  # Core Documentation Directory
│   ├── state_overview.md                  # State Overview
│   ├── constitution.md                    # State Constitution
│   ├── central_government.md              # Central Government Framework
│   ├── ministry_of_magic.md               # Ministry of Magic Introduction
│   ├── higher_education.md                # Higher Education Institutions
│   ├── orbital_facilities.md              # Orbital Facilities Directory
│   ├── supercomputing_systems.md          # Supercomputing Systems
│   ├── academy_of_sciences.md             # Academies of Sciences
│   ├── administrative_summary.md          # Administrative Summary
│   ├── airports.md                        # Overview of Major Airports
│   └── references.md                      # References
├── data/                                  # Data and Raw Materials
│   ├── administrative_divisions.csv       # Administrative divisions data (CSV format)
│   └── administrative_divisions.json      # Administrative divisions data (Flat JSON)
├── scripts/                               # Script Tools
│   ├── json_to_csv.py                     # JSON-to-CSV conversion script
│   └── csv_to_json.py                     # CSV-to-JSON conversion script
├── LICENSE                                # Open Source License
├── README.md                              # Documentation in Chinese
└── README.en.md                           # Documentation in English
```

### Auxiliary Tools
This repository provides two simple Python scripts for two-way conversion between `data/administrative_divisions.json` and `data/administrative_divisions.csv`.
- **Environment**: Requires Python 3 (relies only on standard libraries, no third-party packages needed).
- **JSON to CSV**: Run `python scripts/json_to_csv.py`. It will generate `data/administrative_divisions.csv` with a UTF-8 BOM header for better Excel compatibility.
- **CSV to JSON**: Run `python scripts/csv_to_json.py`. It will convert `data/administrative_divisions.csv` back into `data/administrative_divisions.json`.
- **Custom paths**: `csv_to_json.py` also supports explicit input and output paths, for example `python scripts/csv_to_json.py data/administrative_divisions.csv data/administrative_divisions.custom.json`.

## License
This setting is licensed under the **[CC BY-NC-SA 4.0 License](LICENSE)**. You are free to share, adapt, and build upon the material, **but it must absolutely not be used for any commercial purposes or any illegal actions such as copyright infringement of the original works**, provided you follow these terms:
1. **Attribution**: You must give appropriate credit and indicate that it originated from this archive (by providing a direct link to either the [GitHub](https://github.com/RaidenLumine/federal_republic_of_soul) repository homepage).
2. **ShareAlike**: If you remix, transform, or build upon the material, you must distribute your contributions under the same license.

> **⚠️ Important Disclaimer**:
> This project is an **unofficial, non-profit, fan-made project**.
> Many setting elements in this repository are not entirely original, but rather recontextualizations and amalgamations of multiple existing IPs. **Therefore, unless you sufficiently adapt and originally reconstruct these elements, direct use or derivation may involve copyright issues. We strongly recommend that when creating works based on this setting, you sufficiently adapt, reshape, or generalize the elements you use from specific IPs, stripping them of the defining characteristics of the original IPs to form new, highly original works.**
> This license applies strictly to the **original amalgamated structure and administrative logic** within this repository. All referenced IP elements, their copyrights, and ultimate interpretation rights remain the sole property of their respective copyright holders.

## About the Author
- The setting was originally conceptualized in March 2020 (UTC+8), the idea of archiving it to a code hosting platform was born on March 19th, 2026 (UTC+8), and it was subsequently organized and archived in March 2026 (UTC+8).
- The author views this archive as a "sealed specimen of a thought experiment". **There is no maintenance plan, and no feedback or communication channels are provided, let alone use it for commercial purposes or any copyright infringement activities.**

---
*Archival Version: v1.6*