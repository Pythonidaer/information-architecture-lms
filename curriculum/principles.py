def populate(add):
 add(30,'Separate structure from navigation',[
 ('Define the underlying structure','Learn to distinguish an information architecture from its visible controls. IA defines what content and functions exist, their relationships and the names used to describe them.'),
 ('Choose the right deliverable','An inventory records what exists. An audit evaluates it. A sitemap describes relationships. A navigation specification describes how people move through the interface. These documents answer different questions.'),
 ('Design structure before choosing controls','A menu is one view of an information space. Start with its content and complexity, then prototype suitable controls. A visually attractive menu cannot repair missing content or confusing categories.')],
 'At Cedar Community Centre, “Membership” contains eligibility, prices and renewal. That relationship is IA. Displaying those destinations in a sidebar is navigation. Giving the renewal button a green background is visual design.',
 'Classify these decisions in your notes: merge duplicate price pages; add a breadcrumb; rename “Member services” to “Membership”; increase button padding. Which require understanding the content?',
 'Merging and naming are IA decisions. The breadcrumb is navigation; padding is visual/interaction design. They influence each other. Explain the user need behind each decision rather than treating disciplines as isolated boxes.')
 add(31,'Model one system in different ways',[
 ('Compare three views','Learn when to use a full IA structure, a taxonomy and a navigation model. The structure describes relationships; a taxonomy controls classification; navigation exposes useful routes.'),
 ('Do not force identical models','A navigation menu need not display every taxonomy term or every page. Background classification can support related content and search without becoming a top-level menu.'),
 ('Keep models connected','Give content stable identifiers so the same item can appear in several views. Document which categories, terms and controls refer to that item.')],
 'Cedar has one pottery course record. Its IA parent is Courses. Its metadata includes subject “Arts”, level “Beginner” and venue “West hall”. Navigation exposes Courses and a subject filter, without adding West hall to the main menu.',
 'Describe a beginner coding workshop in three views: its home in the IA, three classification fields, and a visible route to find it.',
 'One possible answer: Courses / Computing / Beginner coding; subject Computing, level Beginner, delivery In person; Courses menu plus subject and level filters. Check that your views all identify the same record. This is an authored example, not a universal model.')
 add(32,'Distinguish finding from discovering',[
 ('Recognise the two goals','Findability concerns something people expect to exist. Discoverability concerns something they encounter without already knowing about it. A product can support one and neglect the other.'),
 ('Match the research question','A task that explicitly names a feature tests finding it. It does not show whether someone would notice that feature during ordinary activity.'),
 ('Support both behaviours','Provide direct routes for known needs and relevant contextual routes for unfamiliar offerings. Do not confuse promotional visibility with useful discovery.')],
 'A member searches for “renew membership”: a finding task. While viewing renewal, they notice reduced fees for carers: discovery. A separate, relevant eligibility link could support that discovery without interrupting renewal.',
 'Choose an expected service and a useful unfamiliar service at Cedar. Write a task to test the first and an observation scenario for the second.',
 'Ask someone to find opening hours. Separately, observe a realistic booking task and see whether they notice accessibility support. Avoid mentioning the support feature in advance if your question is unaided discovery.')
 add(33,'Strengthen information scent',[
 ('Predict the destination','Information scent is the evidence people use to predict whether a route will answer their question. It depends on their current goal, not a link’s wording alone.'),
 ('Align the cues','The label, accompanying description, surrounding context and previous experience all influence expectations. The destination should fulfil the promise made by those cues.'),
 ('Avoid misleading attraction','A tempting label can increase clicks while producing disappointment. Judge whether people reach useful content and complete their task, not whether a link attracts attention.')],
 '“Discover possibilities” offers weak evidence for someone seeking a refund. “Cancel a class and request a refund” predicts the task. Placing it in Booking help strengthens the surrounding context.',
 'Write two labels for Cedar’s cancellation policy. For each, predict what a member would expect after selecting it. Then compare the destination’s heading and opening paragraph.',
 '“Class cancellation and refunds” is a plausible label if both topics are present. “Get your money back” is misleading if refunds depend on a deadline. Preserve the condition in nearby text and test expectations with readers.')
 add(34,'Make search and browsing work together',[
 ('Use complementary routes','Search helps people with a specific query. Navigation exposes the scope of a site and helps people who do not yet know its vocabulary. The balance depends on users and content.'),
 ('Reduce recall demands','Typing a query requires remembering or inventing terms. Browsing lets people recognise available options. Search also depends on result quality and recovery from poor queries.'),
 ('Reconnect results to structure','A result should provide enough context to understand its type and location. Let people continue browsing relevant categories after arriving through search.')],
 'A returning learner searches “pottery Tuesday”. A newcomer browses Courses / Arts because they do not know Cedar’s class names. Both reach the same course record and can inspect related classes.',
 'List three queries for a workshop and two browse routes. Include a synonym and a misspelling. What happens when there are no matching results?',
 'An authored plan could map “coding” and “programming” to the same subject, preserve the query on an empty state and offer related categories. Test actual retrieval before claiming that synonyms or spelling correction work.')
 add(35,'Choose menu size from the content',[
 ('Reject a magic item count','A menu does not become usable simply by containing seven options. Its size should reflect content breadth and the difficulty of recognising meaningful categories.'),
 ('Evaluate the actual options','Consider how distinct and familiar labels are, how much space the pattern provides, and whether people can scan the list. Splitting or combining categories creates tradeoffs.'),
 ('Test representative tasks','Try finding common and less common items. Watch hesitation, mistaken choices and backtracking. Use that evidence to refine grouping rather than meeting an arbitrary count.')],
 'Cedar has five services today. Adding childcare and venue hire could justify more visible categories. Hiding them under “Other” solely to keep five links would reduce the evidence available to visitors.',
 'Propose two top-level menus for Cedar: one with broad groups and one with more specific groups. Predict which tasks each might make harder.',
 '“Activities” may be compact but ambiguous between classes and events. Separate Courses and Events may be easier to recognise. A proposed menu is a hypothesis; compare it using the same tasks and representative participants.')
 add(36,'Balance breadth and depth',[
 ('Compare structural tradeoffs','A broad hierarchy has more choices at each level; a deep hierarchy has more levels. Both can create effort: scanning many choices or repeatedly deciding where to go next.'),
 ('Separate structure from presentation','A multi-level hierarchy can be exposed through a mega menu or through successive category pages. Visible clicks do not directly reveal the underlying structure’s depth.'),
 ('Preserve meaningful groups','Prefer categories people understand over an artificially flat or deep structure. Check information scent along the whole route, not just at the first level.')],
 'One design lists 40 Cedar classes at the top. Another hides Pottery below Activities / Personal development / Creative skills / Arts. A middle option exposes Courses, then Arts, with course links and filters.',
 'Take twelve pieces of content and create a broad version and a deeper version. Choose three tasks, then identify where the visitor must make an uncertain decision.',
 'Your explanation should identify a concrete ambiguous label or overcrowded list. “Fewer clicks is always better” does not justify the choice. Keep the candidate structures for a later tree test.')
 add(37,'Audit common architecture failures',[
 ('Check the structure','Look for absent organisation, disconnected search, missing category landing pages, excessive cross-listing and isolated subsites. These failures prevent people building a useful mental model.'),
 ('Check navigation behaviour','Inspect hidden choices, hard-to-control menus, inconsistency, competing navigation mechanisms and invented labels. Structure and controls need to support the same understanding.'),
 ('Prioritise by consequence','An audit identifies potential problems; it does not establish how often each occurs. Investigate important tasks and record evidence, impact and a proposed next check.')],
 'Cedar’s bookings open on a separate branded site with no route back. Its courses menu disappears there. A member cannot tell whether “Enrichment” contains their class. These are connected integration, consistency and naming problems.',
 'Audit your practice site using the ten failure types across the previous two slides. For each issue, record the affected task, observed evidence and a validation method.',
 'Example entry: “Cancel booking: members cannot locate the external provider’s help; observed in two sessions; add a consistent support route and retest.” Distinguish observed failures from expert-review hypotheses.')
 add(38,'Decide menu count, order and activation',[
 ('Choose a meaningful order','Order categories using the task and context: importance, frequency, sequence or another meaningful scheme. Alphabetical order works best when people already know the terms they seek.'),
 ('Make breadth intentional','Use enough categories to represent the offering clearly. Broad sites may need more options and a different navigation pattern, rather than compressed or ambiguous labels.'),
 ('Provide alternatives to hover','A hover menu needs usable touch and keyboard access. Do not make essential destinations depend on a pointer interaction that some people cannot perform.')],
 'Cedar puts Book a class before its corporate history because booking is a common task. Its full tutor directory is alphabetical because visitors often know a tutor’s name. The same site uses different schemes for different purposes.',
 'Choose an ordering scheme for courses, tutor names and booking steps. Explain why one universal ordering scheme would be unhelpful.',
 'Subject groups can organise courses, alphabetical names can organise tutors, and chronological steps can organise booking. These choices still require recognisable labels and usable access on touch and keyboard.')
 add(39,'Replace the three-click rule with evidence',[
 ('Avoid arbitrary limits','There is no universal three-click threshold for successful navigation. Click count ignores comprehension, waiting, errors and the complexity of the task.'),
 ('Inspect effort between clicks','A short route can still require scanning a huge list. A longer route can feel straightforward when each choice has a clear purpose and provides orientation.'),
 ('Choose useful measures','Combine task success with time, mistakes, backtracking and observed confusion. Reduce unnecessary work without flattening meaningful structure just to meet a number.')],
 'Version A reaches a Cedar refund policy in two clicks through a page of 120 links. Version B takes four clear steps through Booking help and Cancellations. Counting steps alone cannot identify the better experience.',
 'Write a small evaluation plan comparing the two routes. Include a success definition and at least two effort measures.',
 'Define success as finding the correct refund conditions and identifying the applicable deadline. Record time and wrong turns, then ask what was confusing. Keep task wording and content consistent across versions.')
 add(40,'Use polyhierarchy for real ambiguity',[
 ('Understand multiple parents','Polyhierarchy lets an item belong to more than one category. It can support people who reasonably expect the same content in different places.'),
 ('Keep one maintained item','Multiple routes do not require duplicate content pages. Use a stable canonical record and link it from each justified category to avoid conflicting versions.'),
 ('Limit cross-listing','Listing everything everywhere weakens categories and can confuse location cues. Use research to justify alternate routes and define a consistent breadcrumb policy.')],
 'Cedar’s family swimming class is relevant under Swimming and Family activities. Both links can open the same course page. Two independently edited pages could disagree about age limits or fees.',
 'Identify one item that genuinely belongs under two Cedar categories. Explain who benefits, how you would test the routes and how the item would be maintained.',
 'A reasonable proposal uses observed expectations, one content record and explicit category relationships. Do not add a second category merely because it is technically possible; inspect whether people actually look there.')
 add(41,'Turn cross-listing into an implementation rule',[
 ('Connect the concept to a system','A polyhierarchical item has more than one parent relationship. Plan the data and interface together so alternate routes remain understandable.'),
 ('Preserve orientation','Decide whether breadcrumbs follow a canonical path or an appropriate contextual path. Keep the decision consistent and avoid presenting a visitor’s click history as the site hierarchy.'),
 ('Review the extra relationships','Every cross-listing adds maintenance work. Check alternate routes after content moves, and remove relationships that no longer support a useful expectation.')],
 'Record COURSE-17 once, with parent relationships to Swimming and Family activities. Its canonical URL stays unchanged. A navigation specification states how each entry route will display location context.',
 'Draft a three-row specification: content identifier, allowed parent categories and breadcrumb policy. Add one edge case involving entry from an external search engine.',
 'For direct entry, a stable canonical breadcrumb can provide context even without a previous category click. Other policies can work, but must avoid misleading visitors and be tested. Multiple parents are not permission to duplicate inconsistent facts.')
 add(42,'Handle category outliers without overengineering',[
 ('Recognise imperfect membership','People’s categories can tolerate a few loosely fitting items. An outlier does not automatically require a new top-level category or an empty-looking subcategory.'),
 ('Compare the alternatives','Keep the item in a broader group, introduce a useful subcategory, use metadata for alternate discovery, or cross-list where expectations justify it.'),
 ('Consider scale and evidence','The amount of content, distinct user needs and expected growth affect the choice. A theoretically pure classification can be harder to use than a practical one.')],
 'Cedar has twenty regular courses and one equipment-loan guide. A separate “Learning enablement solutions” section adds an unfamiliar category. A recognisable Equipment loans link within course support may fit better.',
 'Choose a location for a single bursary guide. Compare a new Fees and funding subcategory with a direct link from course pages. What future change would alter your decision?',
 'If funding content grows into several distinct tasks, a dedicated category may become useful. With one guide, a clear support location and contextual links could suffice. Record the hypothesis and test finding the guide.')
 add(43,'Write labels with the four Ss',[
 ('Make labels specific and sincere','Specific labels identify the destination. Sincere labels set expectations the destination fulfils. Avoid promises that the content or function cannot meet.'),
 ('Make labels substantial','A label should carry enough meaning to be understood when scanned apart from surrounding text. Preserve distinguishing words instead of relying entirely on nearby copy.'),
 ('Keep labels succinct','Remove words that add no useful distinction. Brevity supports scanning only while the subject, action and important conditions remain understandable.')],
 '“Free courses” is inaccurate when only eligible members receive a waiver. “Course fee support” is more sincere. A short description can explain eligibility before the visitor commits to applying.',
 'Evaluate “Discover”, “Everything about our exciting programmes” and “Evening language courses” against all four Ss. Rewrite the first two for a specific destination.',
 'For a language course directory, “Evening language courses” names subject and schedule without a vague invitation. For an application page, “Apply for course fee support” states the actual action. Confirm each label against its destination.')
 add(44,'Replace ambiguous Learn more links',[
 ('Identify the destination','A standalone “Learn more” label gives little evidence about the next page. Repetition makes scanning and distinguishing links harder, including for assistive technology users.'),
 ('Choose meaningful linked text','Link an informative phrase in the surrounding sentence or write a short destination label. Include format or external-service details when they affect the decision.'),
 ('Preserve relevant context','Descriptive links do not require long labels everywhere. A clear subject and destination can be concise; supporting text can explain conditions without replacing the link’s meaning.')],
 'Three Cedar cards all end “Learn more”. Replace them with “Compare membership prices”, “Check swimming age limits” and “Find accessible facilities”. Each now predicts a different destination.',
 'Write links for a fee table, a cancellation form on another provider’s site and an accessibility policy PDF. Decide what context belongs beside each link.',
 'Possible labels: “Membership prices”, “Cancel a booking on Cedar Bookings” and “Accessibility policy (PDF)”. Add file size only if known and useful. Do not claim that a link submits a cancellation when it merely opens a form.')
 add(45,'Avoid three patterns of weak naming',[
 ('Replace vague invitations','Navigation labels such as “Explore” or “Connect” often conceal the subject. Choose words that help people predict the content or function.'),
 ('Do not force verbal symmetry','Making every menu item a verb or the same grammatical shape can remove useful meaning. Clarity matters more than decorative consistency.'),
 ('Keep personality out of the way','Conversational labels can be friendly yet ambiguous. Use natural language where it helps, while retaining the concrete nouns people need for finding information.')],
 '“Discover / Thrive / Belong” could mean courses, wellbeing services or membership. “Courses / Wellbeing support / Membership” gives visitors more useful distinctions without preventing a welcoming tone elsewhere.',
 'Rewrite Cedar’s menu “Get inspired / Get connected / Get going”. State what content each replacement represents before choosing the wording.',
 'Possible replacements are Events, Contact and Book a class, if those are the actual destinations. A naming exercise cannot resolve undefined categories: establish what each group contains first.')
 add(46,'Build a controlled taxonomy',[
 ('Control classification terms','A taxonomy defines an approved hierarchical vocabulary for classifying content. It differs from free-form tags and from the menu visitors see.'),
 ('Relate the models','A content model defines types and fields. The IA defines the information space. Taxonomy supplies classification rules; navigation uses selected relationships and labels. Thesauri add term relationships; ontologies model richer domain relationships.'),
 ('Build and govern the vocabulary','Inventory terms, involve content experts and users, define preferred terms and scope, test retrieval and assign ownership. Prevent uncontrolled additions from producing duplicate or conflicting categories.')],
 'Cedar’s subject vocabulary permits Computing, Languages and Arts. Editors cannot independently add “IT”, “Tech skills” and “Digital” as competing subjects. Search synonyms can still map those expressions to Computing.',
 'Create a small subject taxonomy with two levels. For one term, write a definition, inclusion/exclusion rule, synonym and owner. Classify three real content items.',
 'Example: Computing includes learning to use or program digital systems, excludes equipment hire, has search synonym IT, and is owned by the course editor. If editors disagree, revise scope notes and test retrieval before expanding the vocabulary.')
