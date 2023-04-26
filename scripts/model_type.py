import enum
import copy


class ModelType(enum.Enum):
    """Collection of Argo model types that can be generated for Workflows, Events, and CD"""

    # Workflows
    workflows = "workflows"

    # Events
    events = "events"

    # CD
    repo_creds = "repo_creds"
    cluster = "cluster"
    account = "account"
    settings = "settings"
    notification = "notification"
    application = "application"
    application_set = "application_set"
    version = "version"
    project = "project"
    certificate = "certificate"
    session = "session"
    gpg_key = "gpg_key"
    repository = "repository"

    @classmethod
    def values(cls) -> set:
        return set([e.value for e in cls])

    @classmethod
    def is_valid(cls, v: str) -> bool:
        return v in cls.values()

    @classmethod
    def is_workflow_type(cls, t: str) -> bool:
        return t in {cls.workflows.value}

    @classmethod
    def is_events_type(cls, t: str) -> bool:
        return t in {cls.events.value}

    @classmethod
    def is_cd_type(cls, t: str) -> bool:
        cd = copy.deepcopy(cls.values())
        cd.remove('events')
        cd.remove('workflows')
        return t in self


