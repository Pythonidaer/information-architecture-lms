from pathlib import Path
import json, html
from curriculum import principles, research, navigation, workshops
from curriculum.checks import CHECKS, FINAL
ROOT=Path(__file__).resolve().parent
sources=json.loads((ROOT/'source-input.json').read_text())
source_map={s['id']:s for s in sources}
coverage={s['id']:[] for s in sources}
decks={}
def deck(id,title,rows,src=None):
 src=src or []
 slides=[dict(id=f'{id}-{i+1}',title=t,body=b) for i,(t,b) in enumerate(rows)]
 node=dict(id=id,type='slides',title=title,slides=slides,sourceIds=src)
 decks[id]=node
 for k in src:coverage[k].append(id)
 return node
def add(key,title,concepts,example,practice,review):
 sid='nng-'+str(key)
 src=source_map[sid]
 rows=concepts+[('Worked example',example),('Try it in your notes',practice),('Review your answer',review),('Read the original',f"[{src['title']}]({src['url']})")]
 node=deck('topic-'+str(key),title,rows,[sid]);node['guideOrder']=src['guideOrder']
for module in [principles,research,navigation]:module.populate(add)
workshops.populate(deck)
def quiz(id,title,rows):
 questions=[]
 for i,(p,opts,exp) in enumerate(rows):
  shift=(i+len(id))%len(opts); rotated=opts[shift:]+opts[:shift]
  questions.append(dict(id=f'{id}-q{i+1}',prompt=p,options=rotated,answer=rotated.index(opts[0]),explanation=exp))
 return dict(id=id,type='quiz',title=title,skill=title,questions=questions)
def section(id,title,ids,check=None):
 children=[decks[x] for x in ids]
 if check:children.append(quiz(id+'-check','Check: '+title.split(' ',1)[1],CHECKS[check]))
 return dict(id=id,type='section',title=title,children=children)
sections=[
 section('start','1 Start',['welcome','cedar-brief'],'start'),
 section('structure','2 Structure and organisation',['topic-'+str(i) for i in range(30,43)],'structure'),
 section('labels','3 Labels and taxonomy',['topic-'+str(i) for i in range(43,47)],'labels'),
 section('cards','4 Card sorting',['topic-'+str(i) for i in range(49,55)],'cards'),
 section('trees','5 Tree testing and diagnosis',['topic-'+str(i) for i in range(55,59)],'trees'),
 section('global','6 Global navigation',['topic-'+str(i) for i in range(59,64)],'global'),
 section('wayfinding','7 Orientation and wayfinding',['topic-'+str(i) for i in range(64,68)],'wayfinding'),
 section('patterns','8 Navigation patterns',['topic-'+str(i) for i in range(68,75)],'patterns'),
 section('mobile','9 Mobile navigation',['topic-'+str(i) for i in range(75,78)],'mobile'),
 section('apply','10 Apply and maintain',['inventory','schemes','map-model','search-workshop','research-plan','accessibility-workshop','migration','governance','capstone'],'apply')]
glossary=[('IA','The relationships, organisation and naming of an information space.'),('Navigation','The interface routes used to reach content and functions.'),('Mental model','A person’s understanding or expectation of how something works.'),('Information scent','Cues used to predict whether a route will satisfy a need.'),('Findability and discoverability','Finding something expected versus encountering something previously unknown.'),('Hierarchy and polyhierarchy','One-parent organisation versus a structure in which some items have multiple parents.'),('Taxonomy and metadata','A controlled hierarchical vocabulary; descriptive data attached to content.'),('Content model','The types, fields and relationships used to represent content.'),('Card sort','A study of how participants group content.'),('Tree test','A task-based evaluation of a stripped-down hierarchy.'),('Dendrogram','A visual representation of clustering under a particular analysis method.'),('Success and directness','Reaching an acceptable destination versus how directly a route is followed; state tool definitions and denominators.'),('Global and local navigation','Major site-wide routes versus routes within a section.'),('Utility and contextual navigation','Supporting tools versus links relevant to the current content or activity.'),('Breadcrumb','A compact representation of location in a hierarchy.'),('Facet and filter','A classification dimension; a constraint that narrows the current result set.'),('Canonical record','The maintained source record referenced through multiple routes.'),('Governance','Ownership and rules for maintaining decisions and responding to change.')]
deck('glossary','Terminology lookup',[(t,b) for t,b in glossary],[])
rows=[('Reading scope','The 46 numbered resources in NN/g’s IA study guide each map to one core lesson, in the recommended order within Principles, Research and Navigation. Applied workshops are additional authored practice. Supplementary research guides are linked for further study; their entire reading collections are outside this course’s scope.')]
for group in ['Principles','Research','Navigation']:
 selected=[s for s in sources if s.get('guideGroup')==group]
 for i in range(0,len(selected),3):
  rows.append((group+' readings '+str(i//3+1),'\n\n'.join(f"{s['guideOrder']}. [{s['title']}]({s['url']})" for s in selected[i:i+3])))
rows.append(('Further research guides','\n\n'.join(f"[{source_map[k]['title']}]({source_map[k]['url']})" for k in ['guide','nng-47','nng-48'])))
rows.append(('Review notes','Sources checked 19 October 2026. The menu checklist now has 17 items although the study guide still says 15. Video summaries were available, not transcripts. The accordion-icon article was available through an indexed excerpt when its direct page failed. Read originals for their full evidence, examples and qualifications.'))
deck('source-directory','Reading directory and coverage',rows,[])
sections.append(section('references','11 Reference',['glossary','source-directory']))
settings=dict(passScore=80,allowRetakes=True,showLessonDetails=False,unlockAll=True,sequential=False,requireLessons=True,brand='#1d70b8',background='#ffffff',surface='#f3f2f1',text='#0b0c0c',muted='#505a5f',border='#b1b4b6',fontScale=1,spacing=24,contentWidth=850,radius=2,font='system',headingFont='system',lineHeight=1.6)
course=dict(schemaVersion=1,id='information-architecture-course-v1',title='Information architecture',description='Organise information, write useful labels, research structures and design navigation. Follow NN/g’s IA reading path with original practice and an applied project.',sections=sections,settings=settings,finalQuiz=quiz('ia-final','Final scenario review',FINAL))
(ROOT/'course.json').write_text(json.dumps(course,indent=2,ensure_ascii=False)+'\n')
for s in sources:
 s['lessonIds']=coverage[s['id']]
 if s['id']=='nng-77':s['reviewStatus']='Indexed article excerpt reviewed; direct page unavailable'
manifest=dict(retrieved='2026-10-19',guide='https://www.nngroup.com/articles/ia-study-guide/',scope='All 46 numbered study-guide resources in order; video page summaries, not full video transcripts. Two supplementary research-guide overviews. Original applied workshops extend the core path. No claim of reproducing full publications or every link beyond this scope.',sources=sources)
(ROOT/'source-manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
scripts=''.join(f'<script src="{s}" defer></script>' for s in ['vendor/marked.umd.js','lesson-markdown.js','lms-runtime.js','voice-config.js','voice-access.js','voice.js'])
page='<!doctype html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#0b0c0c"><meta name="description" content="An independent information architecture course with worked examples, research practice, navigation design and optional private voice tutoring."><title>Information architecture</title><link rel="stylesheet" href="lms.css"><link rel="stylesheet" href="content-theme.css">'+scripts+'</head><body class="lms-export-body"><div id="lms-root"></div><script id="lms-course-data" type="application/json">'+json.dumps(course,ensure_ascii=False).replace('<','\\u003c')+'</script></body></html>\n'
(ROOT/'index.html').write_text(page)
summary=dict(lessonDecks=len(decks),slides=sum(len(n['slides']) for n in decks.values()),knowledgeChecks=len(CHECKS),checkQuestions=sum(len(x) for x in CHECKS.values()),finalQuestions=len(FINAL),coreReadings=46)
(ROOT/'course-stats.json').write_text(json.dumps(summary,indent=2)+'\n')
lines=['# Source coverage','',manifest['scope'],'','| Order | Reading | Lesson | Review |','| --- | --- | --- | --- |']
for s in sources:lines.append(f"| {s.get('guideOrder','Supplement')} | [{s['title']}]({s['url']}) | {', '.join(s['lessonIds'])} | {s['reviewStatus']} |")
(ROOT/'docs'/'SOURCE_COVERAGE.md').write_text('\n'.join(lines)+'\n')
print(json.dumps(summary))
