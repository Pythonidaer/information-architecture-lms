# Information architecture LMS

An independent, self-paced course on organising information, choosing labels, researching structures and designing navigation. Built from the learner and voice setup in [content-design-lms](https://github.com/Pythonidaer/content-design-lms), which uses the shared GraphQL LMS shell.

[Open the course](https://pythonidaer.github.io/information-architecture-lms/) · [Source coverage](docs/SOURCE_COVERAGE.md) · [Project workbook](docs/PROJECT_WORKBOOK.md)

## Course

**59 lesson decks, 429 slides, 10 knowledge checks with 39 questions, and a separate 12-question final scenario review.**

1. Start: outcomes, study approach and the fictional Cedar project.
2. Structure and organisation: IA models, finding/discovery, information scent, search and navigation, menu breadth/depth, myths, polyhierarchy and outliers.
3. Labels and taxonomy: the four Ss, descriptive links, naming mistakes and controlled vocabularies.
4. Card sorting: planning, open/closed/hybrid approaches, wording, recruitment, bias and clustering.
5. Tree testing and diagnosis: tasks, protocol, metrics, paths and choosing complementary methods.
6. Global navigation: menu review, visibility, hidden navigation and audience-based routes.
7. Orientation and wayfinding: direct entry, landmarks, breadcrumbs and local navigation.
8. Navigation patterns: sticky headers, vertical menus, utilities, footers, mega menus and home routes.
9. Mobile navigation: pattern selection, subnavigation and expansion signifiers.
10. Apply and maintain: inventory/audit, organising schemes, sitemap/content model, search/facets, research planning, accessibility, migration, governance and a staged capstone.
11. Reference: terminology and the reading directory.

The 46 numbered resources in [NN/g’s IA Study Guide](https://www.nngroup.com/articles/ia-study-guide/) each have a distinct core lesson, preserving the recommended order within its three categories. Lessons pair concise explanations with original worked examples, a task and reasoned self-check. The final review uses new scenarios rather than repeating the chapter checks. Exercises and the capstone are self-assessed; completion and quiz scores are not professional certification.

All sections start collapsed and every lesson is available. Progress and notes are stored per course in this browser, with reports/CSV, learner settings and Copy entire course. There is no cross-device learner account. Save a separate copy of important work before clearing browser data.

## Source and content scope

Sources reviewed 19 October 2026. See `source-manifest.json` and the generated [coverage table](docs/SOURCE_COVERAGE.md) for all 49 source entries: the main study guide, its 46 numbered readings and two supplementary research-guide overviews. The linked menu article now has 17 guidelines although the study guide calls it 15. Video page summaries were available; video transcripts were not. The accordion-icons article was reviewed through an indexed excerpt because the direct page was unavailable.

The course contains original concise explanations and fictional practice, not complete article text, screenshots or video transcripts. The supplementary qualitative/quantitative guides are further-reading overviews, not a claim to cover every resource in their separate collections. Applied workshops extend the core reading path with authored project guidance. This is not an official NN/g course or an exhaustive treatment of every specialist IA technique.

Content principles come from [llm-instruction-toolkit](https://github.com/Pythonidaer/llm-instruction-toolkit/tree/main/design/content-and-tone) and its [content design reset](https://github.com/Pythonidaer/llm-instruction-toolkit/blob/main/design/ai-design-reset/content-design.md), reviewed at `9e136f976f8b63e9063ac518ec36fdcb0804227a`: meaningful outcomes and headings, plain language, descriptive links, truthful states, useful practice/feedback and no repetitive source disclaimers. Initial tone: conversational but precise, serious, respectful and restrained; feedback identifies reasoning without exaggerated praise. The inherited GOV.UK-inspired palette does not imply government affiliation.

## Private voice on Vercel

The learner course stays public; voice requires server-verified login. It uses WebRTC directly between the browser and OpenAI after the server issues a short-lived token. No local process is needed on Vercel, and no database is required.

1. Import `Pythonidaer/information-architecture-lms` into [Vercel](https://vercel.com/new). Use **Other**, repository root and Node 22. `vercel.json` supplies the static build/output settings and the API function.
2. Add the following **server-only** Production environment variables, then deploy or redeploy:

| Variable | Requirement |
| --- | --- |
| `OPENAI_API_KEY` | Your OpenAI API key |
| `VOICE_PASSWORD` | A unique password of at least 16 characters |
| `VOICE_SESSION_SECRET` | A random secret of at least 32 characters |

Generate a secret on your computer with `node -e "console.log(require('node:crypto').randomBytes(32).toString('hex'))"`. Never commit credentials, expose them through public environment prefixes or paste them into chat. Optional `APP_ORIGIN` pins POST requests to one exact origin without a trailing slash; otherwise the request origin is used.

3. Visit the deployed course and press **Cmd+Shift+L** on Mac or **Ctrl+Shift+L** on Windows/Linux. If intercepted, or on a phone, append `#voice-login` to the URL.
4. Enter your voice password. The microphone SVG icon appears after verification. Open it, select duration and **Alloy** or **Shimmer**, then start. Setup closes when connected; the compact control bar leaves the slide visible. The microphone starts muted until you enable it.
5. Check login, refresh, current-slide reading, lesson changes, microphone control, ending and sign-out on your own device. The tutor receives current-slide text, not screen pixels or private notes. Changing slides supplies new context without automatically requesting speech.

Defaults are `gpt-realtime-2.1-mini`, Alloy, British English accent requested, and 2,048 output tokens per response. Accent delivery is not an exact match to a ChatGPT app voice. Sessions default to one minute with longer options, a 30-second inactivity stop and an approximate $0.10 reported-usage stop. Estimates can lag and are **not a guaranteed billing cap**. OpenAI API billing is separate from ChatGPT subscriptions.

The retained output-budget change previously addressed a token-limit cutoff in the source LMS; real three-minute playback and AirPods behaviour still need device verification on this deployment. Use **Usage and diagnostics → Copy diagnostics** if speech stops. See [monitoring](docs/VOICE_MONITORING.md).

Authentication uses a signed 12-hour HttpOnly/Secure/SameSite=Strict cookie, same-origin JSON POST checks, bounded input, timing-safe verification and instance-local throttling. The hidden login shortcut is only a UI convenience; the token endpoint enforces authentication. Instance-local throttles are not a globally enforced quota. Signing out clears this browser’s cookie and stops its call, but does not revoke copied cookies or other active calls. Rotating the password or signing secret invalidates existing cookies for future requests.

## GitHub Pages and local voice

GitHub Actions builds, tests and publishes an allowlisted static artifact. Pages cannot run the password/token API. For private voice independent of a local helper, use the Vercel deployment.

For local development:

```sh
npm ci
npm run build
npm test
npm start
```

Open `http://127.0.0.1:8787`. The helper can use `OPENAI_API_KEY`, an unsaved modal key, or an explicit opt-in save to `~/.config/information-architecture-lms/voice.json`. The saved file is outside the repository and owner-only; it is not encrypted. The browser does not persist the permanent key. Config status exposes only booleans, and Forget saved key deletes it.

The Pages frontend can use the localhost helper, subject to browser local-network permissions, or a short-lived `ek` token. `npm run token` creates a token using the environment key. Use the same-origin local page if the browser blocks Pages-to-localhost access. The helper trusts localhost and the exact `https://pythonidaer.github.io` origin; it does not serve credential files.

## Editing and checks

Edit `curriculum/*.py` and `source-input.json`, then run `npm run build`. This regenerates `course.json`, embedded `index.html`, `source-manifest.json`, `course-stats.json` and the coverage table. Keep IDs stable when meaning stays the same; changed lesson fingerprints reset that lesson’s saved progress. The Vercel static build packages committed generated files; regenerate them before pushing curriculum changes.

`npm test` checks course readiness, all 46 core readings/order, source mapping, short slides, original final questions, embedded parity, all 429 slides through DOM rendering, completion, notes, reports, progress isolation, authenticated voice access and mocked token/WebRTC lifecycle. Public-output checks exclude helper code and authoring files. No billable calls are made. DOM checks do not establish rendered layout, actual audio delivery or full accessibility: review mobile, zoom, keyboard and your audio device after deployment.

## Future improvements

- Conduct representative learner testing and revise confusing explanations and tasks.
- Add interactive card-sorting and tree-testing practice with transparent scoring and downloadable results.
- Add rendered browser regression coverage when a browser runtime is available.
- Validate three-minute voice playback and investigate any remaining truncation or device issues using diagnostics.
- Add server-side distributed rate limiting if private voice is expanded beyond its current owner.
- Recheck source links and changes periodically; obtain accessible transcripts before expanding video-specific coverage.
