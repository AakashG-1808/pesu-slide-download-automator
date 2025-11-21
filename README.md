# PESU Academy Slide Download Automation

This Python script automates the process of logging into PESU Academy, selecting a course, selecting a unit, opening the first slide, downloading and optionally merging available files using Playwright. All session data is stored only in memory, and the script prompts for your credentials at runtime. It is designed to simplify navigation inside PESU Academy without saving any user data locally.

---

## How to Use

1. Install requirements:  
   `pip install -r requirements.txt`

2. Install Playwright browsers:  
   `playwright install`

3. Run the script:  
   `python app.py`

4. Enter your username and password when prompted.

5. Follow the on screen prompts to choose a course and unit.

---

## Merge PDFs
You can also merge PDFs from any folder using the merge.py script:

`python merge.py --folder "FolderName --output "merged.pdf"`

If merged.pdf already exists, the script will automatically create merged[1].pdf, merged[2].pdf, etc.

`--folder` is not optional
`--output` is optional.