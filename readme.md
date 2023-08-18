### Project Structure:
    .
    ├── data 
    │    ├── round1	               # *.csv datasets: we did not use these as they did not have all the data we needed
    │    ├── round2                # *.csv datasets: used for filter and analysis
    │    ├── round3                # *.csv datasets: used for filter and analysis
    │    └── data_details3.csv     # meta data about the participants we collected data from (shoe type, weight etc.)
    ├── plots                   
    │    ├── report                # plots we used for the report in a separate folder
    │    └── *.png plots           # generated plots
    ├── analysis.py	               # the main script running the project (includes main())
    └── ...	                       # other .py scripts and necessary text files

### Dependencies to install (pip3):
`pandas` <br>
`numpy` <br>
`matplotlib` <br>
`sklearn` <br>
`scipy` <br>
`seaborn`

### After installation:
run `python3 analysis.py`
