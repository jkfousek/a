# vscode keybinds

```json

// Place your key bindings in this file to override the defaults
[
   // Toggle Terminal
   {
      "key": "ctrl+.",
      "command": "workbench.action.terminal.toggleTerminal",
      "when": "terminal.active"
   },
   // Toggle CoPilot
   {
      "key": "ctrl+,",
      "command": "workbench.action.chat.openEditSession",
      "when": "chatEditingParticipantRegistered && view != 'workbench.panel.chat.view.edits'"
   },
   // Settings
   {
      "key": "ctrl+shift+,",
      "command": "workbench.action.openSettings"
   },

]

```
