
class DefaultOnlyMigrationRouter:
    """default のデーターベースだけ migrate 対象とする"""

    def allow_migrate(self, db, app_label, model=None, **hists):
        return db == 'default'
