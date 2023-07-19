import * as vscode from 'vscode';

export function activate(context) {
  // Команда для открытия панели с чатом
  let disposable = vscode.commands.registerCommand('extension.openChat', () => {
    const panel = vscode.window.createWebviewPanel(
      'chatPanel', // Идентификатор панели
      'Chat', // Заголовок панели
      vscode.ViewColumn.Beside, // Место размещения панели (по умолчанию открывается справа от текущей активной панели)
      {
        enableScripts: true // Позволяет использовать скрипты в webview
      }
    );

    // Читаем содержимое файла chat.html и отображаем его в webview
    const chatHtml = vscode.Uri.file(context.extensionPath + '/chat.html');
    panel.webview.html = getWebviewContent(chatHtml);
  });

  context.subscriptions.push(disposable);
}

// Функция для чтения содержимого файла и преобразования его в строку
function getWebviewContent(uri) {
  const path = uri.fsPath;
  const content = fs.readFileSync(path, 'utf-8');
  return content;
}

export function deactivate() { }