# BrainICP-Imaging-Archive

https://doi.org/10.5061/dryad.c2fqz61jh

The "BrainICP Imaging Archive" is a dataset developed for evaluating intracranial pressure from CT brain scans. It includes data from 278 patients with corresponding ICP measurements, demographic, and clinical information. The dataset aims to support the development of AI models for rapid ICP estimation using CT scans. The data acquisition was approved both by the "Ethics & Deontology Committee of University General Hospital of Heraklion"(approval number:1371) and the “Committee of Ethics and Research Deontology of the University of Crete” (approval number: 82/19.05.2023). All subjects were admitted to the neurosurgery department of the University General Hospital of Heraklion between 2012 and 2023.

Description of the data and file structure.

The DICOM files of the patients were preprocessed as illustrated in the figure :

Each patient is mapped to a Python dictionary with the following keys:

         “volume”: 3D array of patient’s slices

        “sex”: patient’s sex

        “age”: patient’s age

        “ICP”: the corresponding ICP value

       “Glasgow Coma Scale”: The GCS of each patient

The "BrainICP Imaging Archive" folder has the following structure:
                
                    BrainICP Imaging Archive
                    |
                    |-- UNDER15_NORMAL
                    |   |-- patients_under15_part1.npy
                    |   |-- patients_under15_part2.npy
                    |   |-- patients_under15_part3.npy
                    |
                    |-- MORE_OR_EQ
                    |   |-- patients_more_or_eq_part1.npy
                    |   |-- patients_more_or_eq_part2.npy
                    |
                    |-- WIDE_RANGE
                        |-- patients_wide_range.npy




