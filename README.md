# Library Management System (`library_manegment`)

A web-based library management system for a faculty library, built as a [Frappe](https://frappeframework.com/) app (Frappe 15 targeted, Python >= 3.10). It catalogues reference items, tracks every physical copy, handles borrowing and returning, and records fines and damages. A small public Vue front end shows the book catalogue.

> The app is spelled `library_manegment` (kept as-is: renaming a Frappe app also changes API paths used by the front end). The inner module is `library_management`.

[العربية](README.ar.md) · [Known issues](docs/KNOWN_ISSUES.md)

## Features

* **Catalogue:** books, magazines, research papers, theses and dissertations, graduation projects, audio, video and electronic items, with authors, publishers, categories and classifications.
* **Physical copies:** one `Item Copy` per physical copy, with its own barcode (`<item barcode>-<copy id>`), status (Available / Unavailable / Damaged) and shelf location (Area / Shelf / Rack).
* **Borrowing:** borrowers are Employees or Students. Loan period and maximum simultaneous loans per role come from the *Faculty Library Setting*.
* **Fines and damages:** a daily job marks late loans *Overdue* and creates a *Delay* fine; reporting damage creates a *Damage* record and a fine equal to the copy price.
* **Membership-based transactions:** a second flow (`Library Transaction`) issues / returns copies for members who hold a valid `Library Membership`.
* **Supply orders** for new items.
* **Public API** for the Vue front end (book list and book details).

## Typical workflow

1. **Set up** the faculty: `Company`, then `Faculty Library Setting` (loan period, delay fine, maximum books per role).
2. **Define places:** `Area` -> `Shelf` -> `Rack` (and `Library Section`).
3. **Define catalogue data:** `Publisher`, `Author`, `Classification`, `Category`.
4. **Add reference items:** `Book`, `Graduation Project`, `Magazine`, ... (the barcode identifies the item).
5. **Create copies:** one `Item Copy` per physical copy (status *Available*, price, location).
6. **Register people:** `Student` and `Employee` (and `Library Member` + `Library Membership` for the membership flow).
7. **Borrow:** create and submit an `Item Borrowing` -> due date is set, loan limit is enforced, the copy becomes *Unavailable*.
8. **During the loan:** *Extend Borrowing*, or *Damage* (creates `Damage` + `Fine`). Every day the scheduler turns late loans into *Overdue* and creates a *Delay* `Fine`.
9. **Return:** the *Returned* button sets the copy back to *Available*.
10. **Retire a copy:** submit an `Unactivation Book` (copy becomes *Damaged*; cancelling restores *Available*).
11. **Public catalogue:** the Vue app lists books via the public API.

## Doctypes (36)

| Area | Doctypes |
|---|---|
| Reference items | Book, Magazine, Research Paper, These And Dissertation, Graduation Project (+ Students, Supervisors), Audio Item, Video Item, E Item |
| Cataloguing | Author, Publisher, Category, Classification, Library Indexing |
| Physical location | Library Section, Area, Shelf, Rack |
| Circulation | Item Copy, Item Borrowing, Library Transaction, Fine, Damage, Unactivation Book |
| People | Student, Employee, Department, Library Member, Library Membership |
| Settings and supply | Company, Faculty Library Setting, Supply Order (+ Items) |

## Public API

Called as `http://<host>:<port>/api/method/<path>`, no login required (`allow_guest`):

* `library_manegment.api.get_all_books.get_all_books`
* `library_manegment.api.get_book_details.get_book_details?book_name=<id>`

## Requirements

* [Frappe](https://frappeframework.com/) 15 (via [bench](https://github.com/frappe/bench))
* Python 3.10 or newer
* MariaDB (the CI workflow tests against MariaDB 10.6)

No other Frappe apps are needed: every Doctype this app links to is defined here (checked with a script; only the built-in `User` and `Language` come from Frappe).

## Setup

```bash
bench get-app <repository-url> --branch <branch>
bench new-site <site-name>
bench --site <site-name> install-app library_manegment
bench start
```

The setup steps follow the standard Frappe flow and have not been run end to end on this branch. The front end lives in the separate `library_vue` repository.

## Branch history

This branch consolidates the team's branches:

| Source | What it contributed |
|---|---|
| `develop` | base: data model, Book / Item Copy / Library Transaction, public API |
| `esmail` | borrowing workflow: Item Borrowing, Fine, Damage, Item Copy price and statuses, delay-fine setting, daily overdue job |
| `manar-branch` | `Department`, `Library Member` and `Library Membership` doctypes, Unactivation Book work, section breaks |
| `main`, `nora` | already contained in `develop` |

Where `develop` and `esmail` changed the same file, the `esmail` version was kept (it is the newest). Details of the fixes made while merging are in the commit messages.

## Team

Commit authors found in the git history of the team repositories: Manar Ahmed, Ibtihal Homadi, Ziad Mansor, Esmail Ebrahim Hamza, Nora Hussain. GitHub organization owner: Shaima Riyadh.

TODO: add each member's role and the project context (course, university, year).

## License

MIT. See [license.txt](license.txt). TODO: fill in the copyright line (`[year] [fullname]`) in `license.txt`.
