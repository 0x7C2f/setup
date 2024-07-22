# plugins/callback/no_skipped.py

from ansible.plugins.callback.default import CallbackModule as DefaultCallbackModule

class CallbackModule(DefaultCallbackModule):
    def v2_playbook_on_task_start(self, task, **kwargs):
        # Suppress skipped tasks
        if task._task.action != 'include' and not task._task.when:
            self._display.display(f"Running task: {task.get_name()}", screen=True)