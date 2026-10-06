# The Archive

**Pair:** Light and Jayden  
**Repository:** https://github.com/jaydeno-afk/archive.git

> This file is Part E of the assignment — **15 marks**.

---

## 1. The record *(3 marks)*

Each manuscript is stored as a dictionary with five fields. The values are read from the CSV file as strings. If a required value is missing or invalid, the record is rejected instead of inventing information.

| Field | Type | Example | If it is unknown, we… |
| --- | --- | --- | --- |
| id | string | `MS001` | reject the record because every manuscript needs a valid identifier |
| title | string | `Tarikh al-Sudan` | reject the record because a title must be present and long enough |
| city | string | `Timbuktu` | reject the record because the city must be one of the recognised cities |
| year | string, converted to integer when needed | `1655` | reject the record because our current system requires a valid year |
| condition | string | `good` | reject the record because the condition must be one of the accepted values |

---

## 2. Our validation rules *(4 marks)*

| Field | Rule(s) | Rejects (example) |
| --- | --- | --- |
| id | Must be exactly `MS` followed by three digits. It is case-sensitive. | `ms001`, `MS1`, `MS00A` |
| title | After removing surrounding whitespace, it must contain at least 3 characters. | `Ab`, `""`, `"   "` |
| city | Must be one of `Timbuktu`, `Djenne`, `Gao`, `Walata`, or `Chinguetti`. The comparison is case-insensitive. | `Kano` |
| year | Must be present, contain digits only, and be between 1100 and 1900 inclusive. | `1099`, `1901`, `c.1590` |
| condition | Must be `fragile`, `fair`, or `good`. The comparison is case-insensitive. | `excellent` |

### Who decided the year range?

We accept the given range of **1100–1900** for this project because it gives the catalogue a clear and consistent scope and makes date validation straightforward.

However, this choice has a cost. Any manuscript dated before 1100 would be rejected even if it were historically important, and a copy made after 1900 would also be rejected even if the text itself was much older. Therefore, the range is useful for this project, but it would be too restrictive for a more complete manuscript catalogue.

---

## 3. The `c.1590` decision *(3 marks)*

**Our choice:** **(a)** Reject it. Only exact years enter the catalogue.

**Why:**  
We chose to accept only exact numeric years because this keeps the year field
consistent and makes operations involving years simple. For example, finding
the oldest manuscript or counting manuscripts before a particular year can
be done by converting the stored year directly to an integer.

A value such as `c.1590` contains additional information indicating that the
date is approximate, so our current validation rejects it rather than
pretending that `1590` is known to be the exact year.

**What it costs us:**  
The disadvantage is that we lose manuscripts whose dates are useful but not
known exactly. A manuscript dated approximately `1590` may still be valuable
to the catalogue, but our current system rejects the whole record. A more
advanced version could store the numeric year together with information about
whether the date is approximate.
---

## 4. Our test table *(3 marks)*

### `validate_year`

| Test data | Value | Expected | Actual | Pass? |
| --- | --- | --- | --- | --- |
| Normal | `1655` | valid | valid | Yes |
| Abnormal | `c.1590` | invalid | invalid | Yes |
| Extreme (low) | `1100` | valid | valid | Yes |
| Extreme (high) | `1900` | valid | valid | Yes |
| Boundary (below) | `1099` | invalid | invalid | Yes |
| Boundary (above) | `1901` | invalid | invalid | Yes |

### `validate_id`

| Test data | Value | Expected | Actual | Pass? |
| --- | --- | --- | --- | --- |
| Normal | `MS001` | valid | valid | Yes |
| Wrong prefix | `XX001` | invalid | invalid | Yes |
| Wrong case | `ms001` | invalid | invalid | Yes |
| Too short | `MS1` | invalid | invalid | Yes |
| Non-digit ending | `MS00A` | invalid | invalid | Yes |
| Empty | `""` | invalid | invalid | Yes |

---

## 5. Collaboration reflection *(2 marks)*

**Jayden:** One thing my partner did that I will steal is working on a separate part of the project while still keeping our work coordinated through branches and pull requests. This showed me how two people can work on the same repository without constantly overwriting each other's work. Reviewing each other's code also helped us catch problems that the person who wrote the code might have missed. One thing I would do differently next time is plan our branch names and division of work more carefully before starting, because we changed which parts we were working on after creating some branches, so a few branch names no longer matched the code being developed on them.

**Light:**One thing Jayden did that I will steal: is researching alot before writing any code and using simple loops and clear checks in most of his codes. One thing I would do differently next time: I would research alot before writing various codes so I can write simpler and more understandable codes

---

## 6. Declaration

- [ ] Both of us can explain every line in this repository.

- [ ] AI assistance was used according to the updated instructions given by our teacher, including help with test generation.

**If you used an AI assistant, say what you asked and what you did with the answer:**

We used an AI assistant to help explain Git and GitHub workflows, validation and testing concepts, identify bugs in code we had written, and suggest useful edge cases.

---

## Running this project

```bash
pytest -v                              # all tests
pytest tests/test_provided.py -v       # the given suite
pytest tests/test_yours.py -v          # your suite
python tools/check_collaboration.py    # your Part C report