#!/usr/bin/env bash
set -euo pipefail

# 1) 准备目录
LOG_DIR="$HOME/yimeng/myLog"
mkdir -p "$LOG_DIR"

# 2) 提示用户输入 comment（下一行输入）
echo "请输入 comment（可留空直接回车）："
IFS= read -r COMMENT || true  # 避免 Ctrl+D 导致脚本退出

# 3) 处理时间戳与文件名
#    MMdd_HHmm = 月日_时分
STAMP="$(date +%m%d_%H%M)"

# 4) 清洗 comment（仅保留字母数字、下划线、连字符和点；空格转下划线）
if [[ -n "${COMMENT// }" ]]; then
  SAFE_COMMENT="$(printf '%s' "$COMMENT" | tr ' ' '_' | tr -cd '[:alnum:]_.-')"
else
  SAFE_COMMENT=""
fi

if [[ -n "$SAFE_COMMENT" ]]; then
  FILENAME="${STAMP}_${SAFE_COMMENT}.log"
else
  FILENAME="${STAMP}.log"
fi

LOG_PATH="$LOG_DIR/$FILENAME"

# 5) 检查是否有 script 命令
if ! command -v script >/dev/null 2>&1; then
  echo "错误：未找到 'script' 命令。请先安装（例如：sudo apt-get install bsdutils 或 util-linux 中的 script）。"
  exit 1
fi

# 6) 开始录制。你可以在该会话中执行操作；输入 exit/Ctrl-D 结束。
echo "开始录制到：$LOG_PATH"
script -f "$LOG_PATH"

# 7) 录制结束后回显绝对路径
echo "已保存到：$LOG_PATH"

