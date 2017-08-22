def bucket_sort(list,min,max):
	num_buckets=len(list)
	buckets = range( 0, num_buckets+1)
	delta = float(max-min)/float(num_buckets)
	out = []
	for bucket in range(0,num_buckets+1):
		buckets[bucket] = []
	for i in list:
		buckets[int((i-min)/delta)-1].append(i)
	for bucket in buckets:
		bucket.sort()

	for bucket in buckets:
		for element in bucket:
			out.append(element)
	return out
list = range(100,1,-1)
print bucket_sort(list,1,100)