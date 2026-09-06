# Question 12

train_labels = ['cat', 'dog', 'bird','cat', 'dog']
test_labels = ['dog','fish','cat','fish','rabbit']

set_train_labels = set(train_labels)
set_test_labels = set(test_labels)

# labels that appear in test but not in train
unique_to_test = set_test_labels - set_train_labels
print(f"Labels that appear in test but not in train: {unique_to_test}")

# common labels between train and test
common_labels = set_train_labels & set_test_labels
print(f"Common labels between train and test: {common_labels}")

# whether test_labels contain duplicate labels or not
has_duplicates = len(test_labels) != len(set(test_labels))
print(f"Test labels contain duplicates: {has_duplicates}")