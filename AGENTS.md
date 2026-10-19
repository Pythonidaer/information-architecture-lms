# Information architecture LMS

Repository: Pythonidaer/information-architecture-lms. content-design-lms at 3c697fc613370c58a03facd7b590eb181497e434 is the shell and voice starting point, not the curriculum source.

Read DESIGN_DECISIONS.md before design changes. Edit curriculum/*.py and source-input.json, then regenerate using npm run build. Preserve all 46 core readings in the NN/g guide's recommended order within Principles, Research and Navigation. Preserve source-to-lesson mapping and explicit source access limitations. Applied workshops are original extensions. Do not publish source article copies, screenshots or inaccessible video transcript claims.

No emojis or text-character icon substitutes. Preserve SVG controls, visible keyboard focus, readable inputs, unpadded numbering, the inherited palette and learner features. All sections begin collapsed and all lessons remain available. Use concise, meaningful slides, useful worked examples and self-checks. Do not repeat boilerplate on every reading slide.

Permanent keys belong only in server environment variables or the explicit opt-in owner-only localhost config at ~/.config/information-architecture-lms/voice.json. Never put credentials, private transcripts, private device traces, slide text or audio in public source, logs or exports. Keep hosted authentication enforced on the server: signed HttpOnly cookies, same-origin JSON POST and fail-closed configuration. A hidden icon is not authorization. Instance-local throttles are not global quotas.

Keep voice optional, explicit, current-slide-only and bounded. Preserve Alloy/Shimmer, default Alloy, shared 2,048-token response budget and current-slide reference updates. Use mocks for automated token and WebRTC tests; no billable test calls. Do not claim actual device playback or full accessibility based on DOM tests.

Run npm run build and npm test; inspect generated parity and public artifact contents before publishing. Report deployment checks separately from device verification.

Voice controls and login must stay disabled on GitHub Pages; hosted private voice is intended for Vercel. Preserve this restriction across learner rerenders.
