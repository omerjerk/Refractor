def write_override_dummy(project_loc):
	OVERRIDE_PLACEHOLDER = "# int in.omerjerk.awesum.MainActivity.getSum(int, int);"
	f = open(project_loc + '/overrides.map', 'w');
	f.write(OVERRIDE_PLACEHOLDER + '\n')
	f.close()