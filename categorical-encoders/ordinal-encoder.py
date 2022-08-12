import numpy as np

def label_encoder(labels_list, return_categories = True):

	unique_labels = sorted(list(set(labels_list)))
	labels_dict = {
		label : int(unique_labels.index(label)) for label in unique_labels
	}
	
	labels = list(map(lambda label : labels_dict[label], labels_list))
	labels_encoded = np.array(labels)

	if return_categories:
		return labels_encoded, labels_dict
	else:
		return labels_encoded
