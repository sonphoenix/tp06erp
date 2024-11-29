{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Manage library authors, books, borrowers, and loans',
    'description': 'A module to manage a library with authors, books, borrowers, and loans.',
    'category': 'Library',
    'depends': ['base','website','hr'],
    'data': [
    'security/library_security.xml',
    'security/ir.model.access.csv',
    'views/library_menu.xml',
    'views/author_views.xml',
    'views/book_views.xml',
    'views/borrower_views.xml',
    'views/loan_views.xml',
    'views/loan_line_views.xml',
    'views/empwizard_views.xml',
    'views/reset_empwizard-views.xml',
    'report/report_defenition_author.xml',
    'report/auteur.xml',
    'report/emprunteur.xml',
    'report/report_defenition_emprunteur.xml',
    'report/emprunt.xml',
    'report/report_defenition_emprunt.xml',
    'views/employee_view.xml',
    'views/article.xml',
    'views/loan_inhirit_report.xml',
    'views/author_inhirit.xml'

    ],

    'installable': True,
    'application': True,
}
