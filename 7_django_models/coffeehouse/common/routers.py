class DatabaseForDevOps(object):
    """
    Determine routing models in for all Django core apps and place in devops database.
    All other models are routed to the next router in the DATABASE_ROUTERS 
    or the default database.
    """

    def db_for_read(self, model, **hints):
        """
        Read operations for all Django core app models go to devops database.
        """
        if model._meta.app_label in ['auth','admin','sessions','contenttypes']:
            return 'devops'
        # Otherwise this router has no opinion on read operations (defer to other routers or default database)
        return None

    def db_for_write(self, model, **hints):
        """
        Write operations for all Django core app models go to devops database.
        """
        if model._meta.app_label in ['auth','admin','sessions','contenttypes']:
            return 'devops'
        # Otherwise this router has no opinion on write operations (defer to other routers or default database)
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations on related models 
        """
        # Allow relations between two models that are both Django core app models
        if obj1._meta.app_label in ['auth','admin','sessions','contenttypes'] and obj2._meta.app_label in ['auth','admin','sessions','contenttypes']:
            return True
        # If neither object is in a Django core app model (defer to other routers or default database)
        elif obj1._meta.app_label not in ['auth','admin','sessions','contenttypes'] or obj2._meta.app_label not in ['auth','admin','sessions','contenttypes']:
            return None
        # Otherwise no opinion (defer to other routers or default database)
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Migration operations for all Django core app models go to devops database.
        """
        if db == 'devops':
            # Migrate Django core app models if current database is devops
            if app_label in ['auth','admin','sessions','contenttypes']:
                return True            
            else:
                # Non Django core app models should not be migrated if database is devops
                return False
        # Other database should not migrate Django core app models            
        elif app_label in ['auth','admin','sessions','contenttypes']:
            return False
        # Otherwise no opinion (defer to other routers or default database)
        return None
