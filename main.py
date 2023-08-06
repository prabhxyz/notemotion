import data_manage

if data_manage.journal_done():
    import graph_page
    graph_page.main()
else:
    import journal
    journal.main()