---
title: 'openSPDM: open-source, FAIR management of simulation data-sets'
authors:
  - name: Mark Norris
    affiliations:
      - openSPDM.org
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

The Challenge of managing simulation data-sets
Today, “the parallel file system is the data management system” for most simulation data. This is neither effective, efficient nor FAIR: Findable, Accessible, Interoperable, Re-usable. For a simulation data-set to be useful and re-useable, it must be complete, it must include all the file data but also the process record which enables peer review, validation and re-use.
Complete simulation data-sets are split between several locations and formats:
●	Bulk data on the parallel file system which is the “data management system [1]” for most users of HPC resources 
●	The Process Record as workflow definition files or written notes on paper or in an office application on a PC
●	Metadata and non-bulk data: simulation configuration and input/output parameters in data files or scripts
●	Textual data buried in reports, in website repositories or/and document management systems 
The dispersion of a data-set across several locations leads to a data-management overhead on expensive expert analysts who must record their activities manually and track and manage the identities and locations of all the files, parameters and documents which define or describe a particular iteration of a simulation. This separation of data files, records, scripts and reports leads to duplicate data entry, for example of a parameter identity and value in a script and in a notebook and then in a report, which is an additional non-value-added activity and a potential source of errors and non-quality. 
Since important information, parameter values, and key results are buried in files in several locations, it’s difficult to either search on complete data-sets or to run Machine Learning (ML),  Artificial Intelligence (AI) or data-mining applications which all need to access the complete data-set including both physical data, parameters, key results and the multi-step process record. Knight et al asserted that fine grained metadata describing physical data, the process by which the data had been derived and the provenance of intermediate and final artifacts are crucially important to understand and explain the results and for the results to be trusted [2]. Eisenhauer et al [3] identified the opportunity that “robustly defined and semantically rich metadata can help us to build software which can more completely address the complexities of scientific data”, however that manually recorded collections  of metadata are fragile: they depend on irregular, implicit connections maintained through labor-intensive, manual processes. 
The data management challenge for Scientific and Engineering workflow datasets can be summarised as the need for a solution which captures user intent, provenance, data and metadata and which can manage in a single database accessible through a single API, as a minimum,  large simulation files, parameters and key-values, granular multi-step process-records and report documents.  
The Opportunity to use SDM technology 
Today, visionary engineering organisations use a novel and unique database design invented by researchers in Munich and first applied at BMW for the management of structural mechanics crash simulations. This data management architecture, called “Simulation Data Management” (SDM), is a breakthrough approach which manages complete simulation datasets by the use of process-data objects, metadata objects and file-data objects combined in a graph structure [4]. This data management approach enables the capture of user intent, thus reducing the time spent by engineers to record their activities. Such an SDM database, a single source of truth accessible through a web browser,  provides a single API to find and access complete data-sets. Process step automation software and scripts can be run on the platform as can data extraction software to extract metadata and key results from bulk-data-files and store them in the database. SDM solutions can also eliminate duplicate data entry, for example of typing parameters both into a script and into a notebook [5], and the errors which this may incur. 
Solution benefits: a holistic SDM data model combining the physical data and the process record in a cloud graph-enabled database: 
•	Captures user intent, provenance and metadata, saving time and eliminating duplicate data entry
•	Provides a single point of access to numerical experimentation data & results
•	Data-sets are Findable, Accessible, Interoperable and re-usable
•	Enables any process to be run against data in any accessible repository - workflow portability.
•	Enables the application of sophisticated surrogate modelling techniques, AI, ML to the analysis of large quantities of historic data
•	Enables effective Information Lifecycle Management: lossy compression or deletion of large files whilst retaining the key results, metadata and the “recipe” to recreate the data if necessary  
Timeliness
Simulation Data Management technology is well understood with two decades of productive experience in leading engineering organisations. The SDM data-model and methods has been instantiated on an agile, open xDM platform. openSPDM, taking advantage of today’s fast CPUs, has been proven to assist analysts and save them time while providing data security and quality assurance for the enterprise.
As research into fusion power moves towards prototype commercial reactors, the number of linked simulations will rise, traceability, reproducibility and validation will become increasingly important. FAIR data management is now urgently required. openSPDM was demonstrated and tested at UKAEA.
The number and size of files produced by numerical simulations is increasing faster than ever with the use of exascale computers. Data storage requirements are now expressed in zettabytes. It is long overdue to manage simulation data-sets effectively to assure FAIRness and eliminate Digital Landfills of data of unknown provenance. 


