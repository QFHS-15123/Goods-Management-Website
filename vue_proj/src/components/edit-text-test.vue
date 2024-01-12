<template>
    <section class="element-box" :style="boxStyle">
        <!--  展示部分-->
        <div
            class="show-text"
            :style="textStyle"
            v-if="!isEdit"
            @dblclick="editText"
            v-html="text"
        ></div>
        <!--  编辑部分-->
        <div ref="text" class="textbox" v-if="isEdit">
            <div
                class="textbox-container"
                contenteditable="true"
                @blur="updateText()"
                id="textbox"
                :style="textStyle"
                v-html="text"
            ></div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'edit-text-test',
    data() {
        return {
            isEdit: false,
            text: '双击编辑文字',
            boxInfo: {
                width: 200,
                height: 36
            }
        }
    },
    computed: {
        //文字的样式
        textStyle() {
            return {
                fontSize: '24px',
                textAlign: 'center'
            }
        },
        //容器的宽高
        boxStyle() {
            return {
                width: this.boxInfo.width + 'px',
                height: this.boxInfo.height + 'px'
            }
        }
    },
    methods: {
        editText() {
            this.isEdit = true
            setTimeout(() => {
                //选中文字
                if (window.getSelection) {
                    let selection = window.getSelection()
                    let range = document.createRange()
                    range.selectNodeContents(document.getElementById('textbox'))
                    selection.removeAllRanges()
                    selection.addRange(range)
                }
                //粘贴时，去除多余格式
                document
                    .getElementById('textbox')
                    .addEventListener('paste', e => {
                        e.preventDefault()
                        e.stopPropagation()
                        let text
                        let clp = (e.originalEvent || e).clipboardData
                        if (clp === undefined || clp === null) {
                            text = window.clipboardData.getData('text') || ''
                            if (text !== '') {
                                if (window.getSelection) {
                                    let newNode = document.createElement('span')
                                    newNode.innerHTML = text
                                    window
                                        .getSelection()
                                        .getRangeAt(0)
                                        .insertNode(newNode)
                                } else {
                                    document.selection
                                        .createRange()
                                        .pasteHTML(text)
                                }
                            }
                        } else {
                            text = clp.getData('text/plain') || ''
                            if (text !== '') {
                                document.execCommand('insertText', false, text)
                            }
                        }
                    })
            }, 100)
        },
        updateText() {
            let modifiedText = this.$refs.text.childNodes[0].innerHTML
                .replace("/<div><br></div>/g", '\n')
                .replace("/<div.*?>/g", '\n')
                .replace("/<br.*?>/g", '')
                .replace("/</div>|&nbsp;|</?span.*?>/g", '')
            this.isEdit = false
            // 文字内容没修改不update
            if (this.text !== modifiedText) {
                if (modifiedText === '') modifiedText = '双击编辑文字'
                this.text = modifiedText
                this.updateBoxSize()
            }
        },
        updateBoxSize() {
            //更新下父容器的高度
            this.boxInfo.height = document.getElementById(
                'textbox'
            ).offsetHeight
        }
    }
}
</script>

<style lang="less" scoped>
.element-box {
    position: relative;
}

.show-text {
    word-break: break-all;
    white-space: pre-line;
}

.textbox {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;

    .textbox-container {
        width: 100%;
        position: absolute;
        border: 1px dashed #000;
        height: auto;
        word-break: break-word;
        outline: none;
        white-space: pre-wrap;
        box-sizing: content-box;
        -webkit-user-select: text !important;
        user-select: text !important;
        -webkit-background-clip: text;
        caret-color: black;
    }
}
</style>