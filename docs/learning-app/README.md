# <App Name> — Learn Something New Every Day

> **Status: draft / template.** This README describes a planned learning mobile app.
> Nothing in this repository implements it yet. Sections marked `<...>` or **TBD** are
> decisions that still need to be made. Replace them before you publish this file.

<App Name> is a mobile app for learning in short sessions. Users work through
bite-sized lessons, review what they learned with spaced-repetition quizzes, and
track their progress over time.

---

## Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Content Authoring](#content-authoring)
- [Accessibility & Localization](#accessibility--localization)
- [Privacy](#privacy)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## Features

| Feature | Description | Status |
|---|---|---|
| Courses & lessons | Courses are split into short lessons (about 3–5 minutes each) that mix text, images, and interactive questions. | Planned |
| Quizzes | Multiple choice, fill in the blank, matching, and true/false questions. Users get feedback right after each answer. | Planned |
| Spaced repetition | Items you got wrong come back for review at increasing intervals. | Planned |
| Progress tracking | Daily streaks, XP, per-course completion, and a history of quiz accuracy. | Planned |
| Offline mode | Downloaded lessons work without a connection. Progress syncs when the device is back online. | Planned |
| Reminders | Optional daily notification at a time the user chooses. | Planned |
| Accounts | Sign up with email or a third-party provider. Guest mode keeps progress on the device only. | Planned |
| Dark mode | Follows the system theme, or the user can set it manually. | Planned |

## Screenshots

_TBD. Add screenshots or a short GIF of onboarding, a lesson, a quiz, and the progress screen._

| Onboarding | Lesson | Quiz | Progress |
|---|---|---|---|
| `<img>` | `<img>` | `<img>` | `<img>` |

## Tech Stack

> **TBD.** Choose one option per row and delete the rest.

| Layer | Options |
|---|---|
| Mobile client | React Native (Expo) · Flutter · native Swift/Kotlin |
| State management | Redux Toolkit / Zustand · Riverpod / Bloc |
| Local storage (offline) | SQLite · WatermelonDB · Hive |
| Backend API | REST or GraphQL service `<link to backend repo>` |
| Auth | `<provider>` |
| Push notifications | Firebase Cloud Messaging / APNs |
| Analytics & crash reporting | `<provider>` (opt-in) |
| CI/CD | `<GitHub Actions / Bitrise / Codemagic>` |

## Getting Started

### Prerequisites

- Git
- The toolchain for the client framework you chose (for example, Node.js LTS + npm for React Native, or the Flutter SDK)
- Xcode (macOS only) to build for iOS
- Android Studio with an emulator or a physical device to build for Android

### Installation

```bash
git clone <repo-url>
cd <repo-folder>

# install dependencies (pick the command for your stack)
npm install            # React Native
# flutter pub get      # Flutter
```

### Run the app

```bash
# React Native (Expo)
npx expo start         # then press "i" for iOS or "a" for Android

# Flutter
# flutter run
```

### Build a release

```bash
# React Native (Expo / EAS)
eas build --platform ios
eas build --platform android

# Flutter
# flutter build ipa
# flutter build appbundle
```

## Project Structure

Suggested layout. Adjust it to match the framework you choose.

```
.
├── src/
│   ├── screens/         # Onboarding, Home, Lesson, Quiz, Review, Progress, Settings
│   ├── components/      # Reusable UI (cards, buttons, progress bars, question widgets)
│   ├── features/
│   │   ├── courses/     # Course & lesson loading
│   │   ├── quiz/        # Question types and answer checking
│   │   ├── review/      # Spaced-repetition scheduling
│   │   └── progress/    # Streaks, XP, stats
│   ├── services/        # API client, auth, notifications, sync
│   ├── storage/         # Offline database & migrations
│   ├── i18n/            # Translation files
│   └── theme/           # Colors, typography, dark mode
├── content/             # Sample course content (JSON/Markdown)
├── assets/              # Images, fonts, icons
├── tests/               # Unit & integration tests
└── README.md
```

## Configuration

Copy the example environment file and fill in your values. **Do not commit real secrets.**

```bash
cp .env.example .env
```

| Variable | Description |
|---|---|
| `API_BASE_URL` | Base URL of the backend API |
| `AUTH_CLIENT_ID` | Client ID for your auth provider |
| `ANALYTICS_KEY` | Optional. Leave this empty to turn analytics off |
| `SENTRY_DSN` | Optional. Used for crash reporting |

## Running Tests

```bash
npm test               # unit tests
npm run lint           # linting & formatting checks
npm run e2e            # end-to-end tests (e.g. Detox / Maestro), if configured
```

Make sure every pull request passes lint and the unit tests. The spaced-repetition
scheduler and the answer-checking logic should have unit tests for edge cases such as
empty answers, differences in case or whitespace, and review dates near time-zone boundaries.

## Content Authoring

Lessons are data, not code, so you can add or update content without releasing a new
version of the app. Here is a suggested lesson format:

```json
{
  "id": "spanish-basics-01",
  "course": "spanish-basics",
  "title": "Greetings",
  "estimatedMinutes": 4,
  "steps": [
    { "type": "text", "body": "\"Hola\" means \"hello\"." },
    {
      "type": "multiple_choice",
      "prompt": "How do you say \"hello\"?",
      "options": ["Adiós", "Hola", "Gracias"],
      "answer": 1,
      "explanation": "\"Hola\" is the most common greeting."
    }
  ]
}
```

## Accessibility & Localization

- Every interactive element needs an accessible label for VoiceOver and TalkBack.
- Support dynamic or large font sizes and keep color contrast at WCAG AA or higher.
- Never use color as the only signal for a correct or wrong answer. Pair it with an icon or text.
- Keep all user-facing strings in `src/i18n/`. Don't hard-code text in components.

## Privacy

- Collect only the data the app needs: account info and learning progress.
- Analytics are opt-in and off by default.
- Users can export or delete their data from **Settings → Account**.
- `<Link to privacy policy>`

## Roadmap

- [ ] MVP: onboarding, one sample course, quizzes, local progress
- [ ] Accounts and cloud sync
- [ ] Spaced-repetition review queue
- [ ] Offline lesson downloads
- [ ] Daily reminders and streaks
- [ ] Leaderboards and social features (optional)
- [ ] Tools for content creators

## Contributing

1. Fork the repo and create a branch: `git checkout -b feature/my-feature`
2. Commit with clear messages and add tests for new logic.
3. Run `npm run lint && npm test`.
4. Open a pull request that describes the change. Add screenshots if the UI changed.

## License

_TBD. For example, MIT. Add a `LICENSE` file and update this section._
