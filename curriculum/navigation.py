def populate(add):
 add(59,'Review menus with the current checklist',[
 ('Make choices visible','The study guide names a 15-point checklist; its linked article now contains 17 guidelines. Review visibility, expected placement, contrast and menus that preserve surrounding page context.'),
 ('Communicate place and options','Indicate the current location and relevant neighbouring pages. Use familiar, front-loaded labels, scannable alignment and suitable access to deeper levels. Optional visual cues support rather than replace text.'),
 ('Make menus operable','Provide usable targets, clear submenu signifiers and reliable touch/keyboard alternatives to hover. Avoid cascading fly-outs, unnecessary pointer travel and novelty. Consider access on long pages without obstructing content.')],
 'Cedar’s menu looks elegant but uses pale text, hides all subjects under an icon and closes when the pointer briefly leaves a narrow target. A structural review alone would miss these interaction failures.',
 'Review your menu under four headings: visibility, location, options and manipulation. Select three high-impact changes and explain the task each would improve.',
 'Example: expose Courses on desktop; mark the current course section; open submenus through a keyboard-operable button. Recheck actual tasks after changing the interface. A checklist identifies risks, not a certificate of usability.')
 add(60,'Make navigation noticeable',[
 ('Design for recognition','A menu must be noticed before it can help. Placement, contrast, styling and visible labels influence whether visitors recognise available routes.'),
 ('Respect familiar locations','Put important navigation where users are likely to look. Avoid making ordinary choices resemble advertising or decorative content.'),
 ('Verify in context','Inspect the page at realistic sizes and during realistic tasks. Do not assume the designer’s knowledge of where a menu lives will transfer to a newcomer.')],
 'Cedar puts course categories inside a photographic banner with no contrasting background. Visitors scan past them as promotion. Moving the same labels into the normal header gives clearer evidence that they are navigation.',
 'Show a page briefly to someone unfamiliar with it. Ask where they would begin finding a class. Record what they noticed before explaining the design.',
 'If they point to search or an unrelated card, investigate why. The observation suggests a question; it does not prove a single cause. Compare a version with clearer positioning and styling using equivalent tasks.')
 add(61,'Understand the cost of hidden navigation',[
 ('Recognise the discoverability tradeoff','Hiding navigation can save space while making options less likely to be noticed or used. NN/g’s study found poorer outcomes for hidden navigation, particularly on desktop.'),
 ('Expose important options when possible','A visible or partly visible menu helps people understand the offering. Limited mobile space may justify a different balance, but does not remove the discovery cost.'),
 ('Measure tasks, not menu clicks alone','A rise in opening the menu could mean engagement or extra work. Examine task success, time, discovery and perceived difficulty together.')],
 'Cedar’s desktop header has room for Courses, Membership and Venue hire. Replacing them all with an unlabelled hamburger reduces visible evidence that venue hire exists.',
 'Propose visible, hidden and combined navigation for Cedar’s phone layout. State which destinations remain exposed and which risk becoming undiscoverable.',
 'A combined version might show Courses and Bookings plus a labelled Menu control. Test whether people find the less visible venue-hire option. Do not generalise one study’s exact numerical effect to every site.')
 add(62,'Preserve global routes across the site',[
 ('Provide persistent scope','Global navigation gives access to major categories and helps visitors understand the site after landing on an internal page.'),
 ('Avoid demoting the whole offering','A single generic dropdown on a spacious desktop layout conceals category choices and adds a step before people can assess them.'),
 ('Evaluate the entire journey','Check direct entry, movement between sections and return routes. A cleaner header can create downstream confusion if it removes useful context.')],
 'A visitor arrives at Cedar’s pottery page from a search engine. Courses, Membership and Visit us in the header communicate the broader service. A lone “Browse” button provides less context.',
 'Open three deep pages on your practice site without visiting the homepage. What can you infer about the organisation and other available services?',
 'Record missing scope cues and routes to related tasks. Check whether a consistent global menu would help before adding more promotional content. The goal is useful access and orientation, not identical headers at any cost.')
 add(63,'Use audience categories only when they help',[
 ('Recognise audience-based navigation','Audience categories organise information around groups such as Students, Tutors or Employers. They can be useful when people identify clearly with a group and its content is distinct.'),
 ('Check overlapping roles','People can belong to several groups or be unsure which applies. Shared tasks may become duplicated or difficult to locate when audience divisions dominate.'),
 ('Compare task and topic routes','Use audience routes alongside other structures when evidence supports them. Test people with overlapping identities and visitors who do not know your organisation’s categories.')],
 'A Cedar tutor who also takes evening classes may not know whether refunds belong under Tutors or Learners. A clear Bookings route can serve the task regardless of role.',
 'Design two candidate routes to a bursary guide: one audience-based and one task/topic-based. Include a person who belongs to more than one audience in your test plan.',
 '“Young learners” may help if eligibility and content differ clearly. “Fees and funding” can support a broader task. Avoid maintaining contradictory versions of the same policy under separate audience sections.')
 add(64,'Show people where they are',[
 ('Support direct entry','Any page can be a visitor’s first encounter. A clear heading, site identity and structural context help people decide whether they reached the right place.'),
 ('Use complementary location cues','Current-section styling, breadcrumbs and local navigation can communicate different levels of location. Make the indication clear without relying only on colour.'),
 ('Test orientation explicitly','Ask visitors where they are, what the page belongs to and where they would go next. A working link alone does not establish orientation.')],
 'The page heading says “Before your first lesson”, while the sidebar identifies Pottery for beginners and the global menu marks Courses. Together the cues place a generic instruction page within a meaningful context.',
 'Choose a deep Cedar page. List its page-level, section-level and site-level cues. Remove one mentally: what ambiguity appears?',
 'Without the course context, a learner might assume instructions apply to all classes. Keep the cues that distinguish scope. Evaluate whether visitors can explain the location without being coached.')
 add(65,'Apply digital wayfinding',[
 ('Create a readable environment','Wayfinding helps people understand their current location and possible routes. Digital equivalents of districts, paths and landmarks can make an information space easier to recognise.'),
 ('Keep landmarks consistent','Stable section names, page identities and navigation placement help people recognise places they have visited. Arbitrary changes can break that continuity.'),
 ('Provide recovery routes','Visitors should be able to move up, change direction or return to a useful starting point. An unfamiliar deep page should not become a dead end.')],
 'Cedar uses a consistent course title as a landmark across overview, timetable and preparation pages. Local navigation connects the pages. A Courses link offers a route back to the wider collection.',
 'For your practice site, identify a district, a landmark and a recovery route. Explain how each differs from decoration.',
 'A named course section is a district; its persistent title can be a landmark; a parent category link supports recovery. Their value depends on helping people understand and move, not on mimicking a physical map literally.')
 add(66,'Design useful breadcrumbs',[
 ('Represent location, not history','Breadcrumbs show a meaningful path within the hierarchy. They supplement global and local navigation. On polyhierarchical sites, choose one coherent path rather than showing every possible parent.'),
 ('Link actual destinations','Start with Home where appropriate, include real parent pages and end with the current page as nonlinked text. Avoid phantom categories that have no destination.'),
 ('Adapt to small screens','Do not shrink targets into unreadable text or wrap a long trail awkwardly. Consider showing fewer nearby levels. Breadcrumbs add little to a very shallow or purely linear site.')],
 'For Cedar’s pottery preparation page, a useful ordered trail is Home, Courses, Pottery for beginners, Before your first lesson. It describes structure even when someone arrives directly from a search engine.',
 'Write breadcrumbs for a page with two possible parents. Choose a policy and explain the phone version. Check that every linked parent is a real page.',
 'A canonical course path is one defensible choice. A shorter phone trail might expose the immediate parent with a clear label. Verify context, target usability and consistency rather than blindly retaining every level.')
 add(67,'Use local navigation for nearby content',[
 ('Show the neighbourhood','Local navigation exposes pages within the current section. It supports orientation and comparison without forcing repeated trips back to a parent page.'),
 ('Distinguish global and local choices','Global navigation moves between major sections. Local navigation provides relevant detail within one. Give the local group a meaningful heading and identify the current page.'),
 ('Keep it manageable','Expose useful siblings and parents without dumping the entire site tree into a sidebar. Adapt presentation for narrow screens while preserving access.')],
 'A Cedar course sidebar offers Overview, Dates and fees, Before you arrive and Accessibility. Learners can compare preparation and access information without repeatedly returning to the course overview.',
 'Choose five useful local destinations for venue hire. Which belong in global navigation or in the page body instead?',
 'Room options, Prices, Availability and booking, Equipment and Access could form local navigation. Membership is a global alternative; a specific cancellation deadline belongs in policy content, possibly linked contextually.')
 add(68,'Keep sticky headers useful and unobtrusive',[
 ('Decide whether persistence helps','A sticky header keeps controls available during scrolling. Use it when repeated access benefits the task; it also consumes space and can obstruct content.'),
 ('Control size and contrast','Keep persistent chrome compact and distinguish it from the content beneath. Check that headings, focused controls and anchor destinations remain visible.'),
 ('Avoid distracting movement','Use minimal, predictable motion. A partially persistent header may be appropriate, but appearing and disappearing controls should not interfere with reading or interaction.')],
 'Cedar’s phone header occupies almost half the screen after the menu and voice bar open. A compact header with the active voice controls in normal flow leaves more room for the lesson or booking content.',
 'Inspect a long page while scrolling and enlarging text. Note any content hidden by the header, keyboard focus obscured or jump-link destinations covered.',
 'Reduce unnecessary height, provide suitable scroll spacing and reconsider persistence if it does not support the task. Test the combined state with banners, navigation and optional voice controls visible.')
 add(69,'Choose vertical navigation for a broad structure',[
 ('Recognise its strengths','A left-side vertical menu can accommodate more categories and longer labels than a constrained horizontal bar. It is familiar and supports scanning and growth.'),
 ('Accept its space cost','The sidebar consumes width. Evaluate the content area and responsive behaviour rather than squeezing the same structure into every screen.'),
 ('Make the list scannable','Left-align labels, put distinguishing words early and keep the menu visible. Separate levels clearly and avoid reducing readability to make everything fit.')],
 'Cedar’s staff learning portal has twelve subject areas with descriptive names. A left sidebar accommodates them without tiny text. On a phone, a labelled course-outline control exposes the same subjects.',
 'Compare a horizontal bar and vertical list using the same twelve labels. Identify where truncation or compression would change meaning.',
 'If “Support for course tutors” becomes “Support”, the saved space sacrifices useful distinction. Consider a vertical pattern or different grouping before changing the label. Validate scanning and narrow-screen access.')
 add(70,'Plan vertical navigation states',[
 ('Separate pattern from hierarchy','A vertical list can represent global or local navigation. Its direction does not determine the information architecture or which levels should be exposed.'),
 ('Specify expansion and selection','Show which groups expand, which destinations navigate and which page is current. Avoid one ambiguous target doing different things depending on where it is clicked.'),
 ('Handle long lists deliberately','Consider scrolling, section grouping and preservation of position. Keep keyboard access and orientation intact when the selected page changes.')],
 'Cedar’s LMS outline has section disclosures and lesson links inside them. Opening a section exposes choices; selecting a lesson changes content. These actions should remain distinct and consistently labelled.',
 'Write a state specification for a course sidebar: collapsed group, expanded group, current lesson and narrow-screen drawer. State what happens to focus when it closes.',
 'A drawer should return focus to its trigger when closed. Current-page meaning should be exposed to assistive technology as well as visually. Do not claim a sidebar is accessible without testing its actual interaction.')
 add(71,'Place utility navigation where it is needed',[
 ('Identify supporting tools','Utility navigation provides actions such as sign in, contact, save, print or change view. These tools support use of the site rather than define its main subject categories.'),
 ('Group and place by purpose','Use expected locations and distinguish account tools from primary categories. Put contextual tools near the content they affect when that improves understanding.'),
 ('Use clear labels and states','Recognisable icons may support tools, but require accessible names. Explain state changes and show only actions that are actually available.')],
 'Cedar’s public categories are Courses, Membership and Visit us. Sign in belongs with account tools. Print this timetable belongs near the timetable. A voice icon appears only after the server verifies private access.',
 'Classify Notes, Courses, Sign out, Contact and Print timetable. Decide where each should appear and what its label must explain.',
 'Courses is primary navigation. Sign out is an account utility. Notes and Print are contextual tools; Contact may be global utility or a primary task depending on the service. Document the reason for each placement.')
 add(72,'Give the footer a deliberate job',[
 ('Support expected secondary routes','Footers often contain contact, help, legal information and other supporting destinations. Visitors may look there intentionally or after failing to find a route elsewhere.'),
 ('Choose a pattern for the content','A compact footer, grouped doormat navigation, site-map links, secondary tasks or contextual footer serve different needs. Do not add a large footer solely to imitate another site.'),
 ('Keep it reachable','Infinite scrolling can make the footer impossible to reach. Promotional modules should not obscure necessary links. Maintain the same labelling care used in the main menu.')],
 'Cedar’s footer groups Contact, Accessibility and Privacy, plus a clear Venue hire route. A long events feed provides a stable way to reach footer information rather than continually pushing it away.',
 'Design a small footer inventory. For each item, record its user need and whether another route should also exist. Remove one item with no clear purpose.',
 'Important accessibility support may need contextual links as well as a footer route. The footer is useful redundancy, not a place to hide content essential to booking. Verify that visitors can reach it by keyboard and on a phone.')
 add(73,'Use mega menus for grouped choices',[
 ('Expose useful levels together','A mega menu presents multiple grouped choices in a large panel. It can reveal categories and subcategories at a glance without forcing deep cascading menus.'),
 ('Organise the panel','Use meaningful group headings, clear typography and orderly placement. Keep the choices understandable without promotional images or colour alone.'),
 ('Specify reliable interaction','Support click/tap and keyboard access, predictable closing and manageable focus. Pointer hover should not be the only route. Plan an alternative for smaller screens.')],
 'Cedar’s Courses panel groups Arts, Computing and Languages with several popular subjects beneath each. Its full directory remains reachable. An unrelated membership promotion would compete with the menu’s finding task.',
 'Sketch the content specification for a mega menu using three groups and nine destinations. Write the small-screen fallback and the keyboard behaviour.',
 'A nested disclosure or category landing page can expose the same destinations on a phone. Do not merely shrink the desktop panel. Ensure that group headings and actual destination links are distinguishable.')
 add(74,'Make the route home recognisable',[
 ('Use convention deliberately','People often expect a site’s logo or identity at the upper left to return home. NN/g’s study found that centring the logo made returning home harder in its tested designs.'),
 ('Separate branding from navigation evidence','Aesthetic preference or brand recall does not establish that visitors recognise a home link. Check placement, accessible naming and additional home routes.'),
 ('Test the relevant context','Do not treat a study’s exact effect size as a universal prediction. Include direct entry and recovery tasks across the layouts your audience uses.')],
 'Cedar places its linked identity at the top left and supplies a clear Home destination where useful. A mobile layout preserves an understandable route instead of assuming a decorative centred mark will be recognised.',
 'Open a deep page and ask someone to return to the site’s starting point. Record the first action, hesitation and whether the route was understood.',
 'If the identity is mistaken for decoration, inspect its placement and accessible name. An explicit Home link can provide another route. Avoid making users depend on a convention they cannot perceive.')
 add(75,'Select a mobile navigation pattern',[
 ('Balance visibility and space','Mobile navigation needs to remain discoverable and operable without consuming the content area. The best balance depends on the offering and frequent tasks.'),
 ('Compare the main approaches','Visible navigation or tab bars expose a limited set of destinations. A menu drawer can hold more but hides choices. A navigation hub uses a page to present routes with more context.'),
 ('Keep essentials recognisable','Prioritise meaningful destinations, clear labels and usable targets. Preserve access to less frequent tasks and test whether hidden options are found.')],
 'A compact Cedar booking app might expose Courses, My bookings and Account. A broad public site may need a labelled menu and useful category pages rather than trying to fit every category in a bottom bar.',
 'Choose a pattern for Cedar’s public site and its returning-member booking tool. State the top tasks and the cost of your choice.',
 'Different products can justify different patterns. A bar with three frequent destinations can support returning members, while a public site needs to reveal a broader offering. Evaluate the hidden routes rather than treating them as solved.')
 add(76,'Preserve context in mobile subnavigation',[
 ('Handle more than one level','Mobile subnavigation reveals choices within a section. Common patterns include accordions, sequential menus, section menus and subnavigation hubs. Each trades visible context against space and interaction effort.'),
 ('Make movement clear','People should distinguish opening a group, visiting a category page and moving back a level. Provide current section context so a new panel does not feel like an unrelated page.'),
 ('Avoid ambiguous split actions','A parent label that navigates while a tiny adjacent icon expands can be confusing. Use a clear, testable interaction and ensure parent overview content remains reachable.')],
 'Cedar’s phone menu opens Courses, then Computing. The panel heading identifies Computing and a labelled Back to Courses control reverses the level. “Computing overview” remains a real destination.',
 'Specify how someone reaches a third-level course and then moves to a sibling subject. Include expansion, page navigation and back behaviour.',
 'A sequential menu can retain a visible title and parent route. An accordion can retain surrounding categories but grow long. Test whether visitors understand both location and next action, including with keyboard and screen reader.')
 add(77,'Distinguish expansion from navigation',[
 ('Use a clear signifier','NN/g’s accordion-icon research found the caret more clearly communicated expansion in place than the alternatives it tested. A signifier is a cue to an action, not the action itself.'),
 ('Align cue and behaviour','An expanding control should expose its state and operate consistently across its label and icon. Do not present a familiar expansion cue that unexpectedly navigates elsewhere.'),
 ('Test more than recognition','Comprehensible icons do not establish keyboard operation, focus handling or content discoverability. Keep meaningful text and test the whole control.')],
 'In Cedar’s outline, “Research methods” and its SVG caret form one disclosure target. Selecting it reveals lessons. The separate “Card sorting” link opens a lesson. A screen reader can identify the disclosure’s state.',
 'Write a control specification with its accessible name, action, expanded state and keyboard operation. How will a user know whether selecting it changes the page?',
 'A button can expand a group and expose aria-expanded; a link can navigate to a destination. Native details/summary may suit a simple disclosure. Choose semantics based on behaviour and verify the actual implementation.')
