run-tests:

	@echo "Running lettuce tests"
	#python manage.py harvest tests/lettuce_selenium_tests --settings=conf.settings_lettuce
	lettuce functional_tests/features/
