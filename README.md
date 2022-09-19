# Data_inference

**Objective**<br />
1. For a given pair of label tags (annotated(A) and predicted(P)), find and display the examples of sentences where a dependency relation A is being predicted wrongly as P.
2. Display a table with the Sanskrit and English meaning of both the tags respectively.
3. Display 3 ground-truth examples from the training data for each of the tags.

**conf_mat.csv**<br />
confusion matrix - confusion between the data labels (hdtb test data file and predicted file)
each cell is the number of times the row header is confused as the column header.

**result_file.csv**<br />
prediction file obtained using diaparser

**final_file1.csv**<br />
test data file with only required columns along with added columns - DOC_NO, SENT_ID, ID (word ID within sentence)
**Note** - In the code, this file is added with columns having corresponding predictions (head and dependency relation) from the predicted file.

**label_meanings.csv** <br />
Contains kaaraka labels used in the dataset and their meanings in Sanskrit and English

**final_file_train.tsv**<br />
https://drive.google.com/file/d/1uXL47zPQO3TF616m-ZmcKQf7j3TIeHoi/view?usp=sharing<br />

file used to display some ground-truth examples for labels.

**test_sent.csv**<br />
mapping of sentence IDs with the complete sentences.
