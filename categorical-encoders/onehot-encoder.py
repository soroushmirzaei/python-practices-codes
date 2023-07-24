import numpy as np

def label_encoder(labels_list, return_categories = True):

	unique_labels = sorted(list(set(labels_list)))
	labels_dict = {
		label : int(unique_labels.index(label)) for label in unique_labels
	}
  
	labels_encoded = list()
	for label in labels_list:
    	label_encoded = len(unique_labels)*[0]
    	label_number = labels_dict[label]
    	label_encoded[label_number] = 1
    	labels_encoded.append(label_encoded)
    	labels = labels_encoded
  
  	labels_encoded = np.array(labels)
  
  	if return_categories:
		return labels_encoded, labels_dict
	else:
		return labels_encoded
