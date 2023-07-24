import numpy as np

def label_encoder(labels_list, return_categories = True, normalize = True):

	labels = list()
	for item in labels_list:
		for element in item:
			labels.append(element)

	unique_labels = sorted(list(set(labels)))
	labels_dict = {
		label : int(unique_labels.index(label)) for label in unique_labels
    }

    labels_encoded = list()
    for labels in labels_list:
        label_encoded = len(unique_labels)*[0]
        for label in labels:
            label_number = labels_dict[label]
            label_encoded[label_number] = 1
        if normalize:
            label_encoded = [var/sum(label_encoded) for var in label_encoded]
        labels_encoded.append(label_encoded)

    labels_encoded = np.array(labels_encoded)
    
    if return_categories:
        return labels_encoded, labels_dict
    else:
        return labels_encoded
