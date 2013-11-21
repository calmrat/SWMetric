Bachelors Thesis: 
=================

Software Quality and Contribution Quality Metrics, Analysis and Visualization
*****************************************************************************

Student: Radim Špigel
Advisor: "Chris Ward" <cward@redhat.com>
Advisor: "Juraj Niznan" <jniznan@redhat.com>

Start Date: 11-01-2013
Due Date: FILL ME IN
 

Abstract
--------
 
Using free and open source software – focusing on existing development tools and libraries available within the python 3 pip, scientific computation, process distribution and publication stacks, along with modern web-browser based d3.js data driven visualization technologies – build a tooling pipeline to automatically extract, analyse and derive various software “quality” and “quality contribution” metrics for broad range of existing free and open source, Python based software projects – including core metrics such as commits made, lines added and removed, commit and author contribution frequency, etc; along with experimental metrics, such as retrospective commit quality score and defect contribution probability – using raw source-code available in Git source-code management repositories and meta-data generated as a by-product of managing software development in Git overtime, at both an individual repository level and at scale across hundreds of Git repositories in aggregate – publishing a short, written analysis of select python projects found on git.fedorahosted.org and pkgs.fedoraproject.org for public review and comment, along with the source code required to reproduce the result, under a GPL or with an otherwise open source license variant of choice.
 

Description
-----------

Fedora, a leading community driven, Red Hat sponsored, Free and Open Source Linux based distribution is comprised of tens of thousands of packages and millions of lines of code, contributed by a diverse and vibrant community of thousands of individuals and organizations across the globe.

To manage the source code that makes up the distribution, Fedora uses Git. Git is a relatively new, free and open source distributed version control system that has quickly become the “gold standard” for source code management across the Open Source community and beyond.

Every week, changes to hundreds, perhaps thousands of lines of code are committed to the many project Git repositories underlying Fedora; new features are implemented, tests cases written, documentation enhanced, and defects are fixed, just to name a few examples of the types of changes occuring day in and day out.

Maintaining project code quality, despite this constant change, is a critical function in determining the success or failure of a given software project. Over the past decades, poor code quality has led to countless examples of the downfall of businesses and in some cases, even lives. Overlooked, misunderstood and undervalued issues of software quality are a constant threat to our well-being and becoming more so every day.

Making changes to a given project or a broader collection of interdependent projects is necessary for progress to be made, but it must be acknowledged that even when contributors work is intended to fix existing defects, among the many other examples of the types of changes one might make, each and every change inherently increases the probability that new defects or incorrect behaviors will be introduced as well and do everything in our power to catch and correct defects and other issues with code that cause unexpected and incorrect behavior to occur.

The importance of maintaining software quality assurance is made even clearer when we consider the fact that a significant portion of the code committed and used by millions of people everyday comes from volunteers with very little or absolutely no oversight of the code they’re contributing!

This project “Software Quality and Contribution Quality Metrics, Analysis and Visualization with Git, Python and d3.js” is intended to be a small, simple experiment in building meaningful quality metric models to measure and assign software quality ‘scores’ of source code contributions and the contributors overtime, based purely on the data generated within the context of managing project source code and development workflows with Git.

The resulting methods, if viable, are expected to complement the already well established, more traditional methods of measuring and detecting software quality issues, such as code reviews, static analysis and execution of test scenarios we have collectively relied on to uncover defects in the software we produce, since the beginning of the digital age; not replace them.

Project Breakdown
-----------------
The first stage of this project will be to develop (or incorporate) tools to collect and aggregate git commit objects and other meta-data, generated as a by-product of using Git to manage the software development workflows and source code contributions over time, across a broad range of Open Source projects publicly hosted by Fedora community. Specifically, git.fedorahosted.org and pkgs.fedoraproject.org. Estimated time of completion: 40 hours.

The second stage will be to develop a handful of high-level, generic Git metrics, along with reproducible analysis and visualization pipelines that facilitate exploration of Git data that we believe might increase our understanding and intuition of the ‘context’ surrounding project quality features found in individual project repositories and in aggregate. Some examples of metrics we are considering at this time include (but are not limited to) code churn and volatility, contributer distribution and commit frequency patterns. Estimated time of completion: 40-80 hours.

The third stage of the project will be to develop two experimental ‘quality’ and ‘quality contribution’ proxy measurements. Currently, we have loosely defined the following two ‘strawman’ metrics proposed to start, which might very well change, depending on the results of the investigation work completed during the first two stages. Currently, they will be referred to as “Retrospective Commit Quality Score” and “Defect Contribution Probability”. Estimated time of completion: 40 hours.

The goal of “Retrospective Commit Quality Score” is to provide a consistent, objective measure of the ‘quality’ of a given commit – and commits, in aggregate – using some form of a calculation based on a simple premise that lines of code commited and later removed are positive indication of negative code quality.

The goal of “Defect Contribution Probability” is similar, but will use the ‘retrospective commit quality scores’ calculated above, aggregated across projects, per author to derive an probability score that a given commit includes low quality lines of code; i.e. will be later removed.

The fourth and final stage of this project is to write an assessment of the results for this project in English and publish it for review and comment in a public forum. Estimated time of completion: 40 hours.


Educational Aims
----------------
To complete this project, the student is expected to understand the fundamentals of:
* Git – a free and open source distributed version control system
* managing git repositories, distributed processing, data mining, data analysis and data visualization with python 3
* data visualization with d3.js
* current and on-going research in the field of software quality analysis
