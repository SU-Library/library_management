[Readme باللغة العربية](README.ar.md)

# Library Management System

The Library Management System is a comprehensive web-based solution designed to streamline the administrative processes involved in managing a faculty library. It covers cataloguing, tracking physical copies, borrowing and returning, and recording fines and damages.

## Overview

The system leverages the [Frappe framework](https://frappeframework.com/), known for its flexibility and power in building complex web applications. It addresses key library needs, including:

* Reference Catalog Management: Manages books, magazines, research papers, theses and dissertations, graduation projects, and audio, video, and electronic items, with authors, publishers, categories, and classifications.
* Copy Tracking: Tracks each physical copy of a reference item, its barcode, and its status (Available, Unavailable, Damaged).
* Borrowing and Returns: Handles borrowing and returning of copies by employees and students, with a loan period and a maximum number of loans per role.
* Fines and Damages: Records delay fines (created by a daily job) and damage reports with their fines.
* Physical Location: Organizes copies by library section, area, shelf, and rack.
* Supply Orders: Manages supply orders and their items.

## Technology Stack

* Framework: [Frappe](https://frappeframework.com/) (version 15 targeted)
* Backend: [Python](https://www.python.org/) 3.10 or newer
* Frontend: JavaScript (Frappe forms) and Vue (public catalogue, separate repository `library_vue`)
* Database: [MariaDB](https://mariadb.org/)

## Required Apps

The Library Management System does not require any additional Frappe apps. It depends only on the Frappe framework.

## License

This system is licensed under the MIT License. See [LICENSE](license.txt) for more information.
