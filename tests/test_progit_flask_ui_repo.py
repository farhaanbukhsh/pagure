import pagure.lib
class PagureFlaskRepotests(tests.Modeltests):
    """ Tests for flask app controller of pagure """
        super(PagureFlaskRepotests, self).setUp()
        pagure.APP.config['TESTING'] = True
        pagure.SESSION = self.session
        pagure.ui.SESSION = self.session
        pagure.ui.app.SESSION = self.session
        pagure.ui.repo.SESSION = self.session
        pagure.APP.config['GIT_FOLDER'] = tests.HERE
        pagure.APP.config['FORK_FOLDER'] = os.path.join(
        pagure.APP.config['TICKETS_FOLDER'] = os.path.join(
        pagure.APP.config['DOCS_FOLDER'] = os.path.join(
        self.app = pagure.APP.test_client()
        with tests.user_set(pagure.APP, user):
        with tests.user_set(pagure.APP, user):
        with tests.user_set(pagure.APP, user):
        with tests.user_set(pagure.APP, user):
        repo = pagure.lib.get_project(self.session, 'test')
        msg = pagure.lib.add_user_to_project(
        with tests.user_set(pagure.APP, user):
        with tests.user_set(pagure.APP, user):
        with tests.user_set(pagure.APP, user):
        with tests.user_set(pagure.APP, user):
        with tests.user_set(pagure.APP, user):
                '<title>Overview - test - Pagure</title>' in output.data)
        repo = pagure.lib.get_project(self.session, 'test')
        item = pagure.lib.model.Project(
        repo = pagure.lib.get_project(self.session, 'test')
        item = pagure.lib.model.Project(
    def test_view_commits(self):
        """ Test the view_commits endpoint. """
        output = self.app.get('/foo/commits')
        output = self.app.get('/test/commits')
        output = self.app.get('/test/commits')
        output = self.app.get('/test/commits')
        repo = pagure.lib.get_project(self.session, 'test')
        output = self.app.get('/test/commits')
        output = self.app.get('/fork/pingou/test/commits?page=abc')
        item = pagure.lib.model.Project(
        output = self.app.get('/fork/pingou/test3/commits/fobranch')
        output = self.app.get('/fork/pingou/test3/commits')
        item = pagure.lib.model.Project(
        item = pagure.lib.model.Project(
            '<span style="color: #00A000">+ Pagure</span>' in output.data)
        item = pagure.lib.model.Project(
            '<span style="color: #00A000">+ Pagure</span>' in output.data)
index 0000000..fb7093d
@@ -0,0 +1,16 @@
+Pagure
+Pagure is a light-weight git-centered forge based on pygit2.
+Currently, Pagure offers a web-interface for git repositories, a ticket
+system and possibilities to create new projects, fork existing ones and
+create/merge pull-requests across or within projects.
+Homepage: https://github.com/pypingou/pagure
        item = pagure.lib.model.Project(
index 0000000..fb7093d
@@ -0,0 +1,16 @@
+Pagure
+Pagure is a light-weight git-centered forge based on pygit2.
+Currently, Pagure offers a web-interface for git repositories, a ticket
+system and possibilities to create new projects, fork existing ones and
+create/merge pull-requests across or within projects.
+Homepage: https://github.com/pypingou/pagure
        item = pagure.lib.model.Project(
        with tests.user_set(pagure.APP, user):
        with tests.user_set(pagure.APP, user):
            item = pagure.lib.model.Project(
            item = pagure.lib.model.Project(
            item = pagure.lib.model.Project(
            item = pagure.lib.model.Project(
    SUITE = unittest.TestLoader().loadTestsFromTestCase(PagureFlaskRepotests)