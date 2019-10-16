// 按钮点击事件
$(function() {
        $('#start-bg-job').click(start_long_task);
    });
    
    // 请求 longtask 接口
    function start_long_task() {
        // 添加元素在html中
        div = $('<div class="progress"><div></div><div>0%</div><div>...</div><div>&nbsp;</div></div><hr>');
        $('#progress').append(div);
    
         // 创建进度条对象
        var nanobar = new Nanobar({
            bg: '#44f',
            target: div[0].childNodes[0]
        });
    
        // ajax请求longtask
        $.ajax({
            type: 'POST',
            url: '/longtask',
            // 获得数据，从响应头中获取Location
            success: function(data, status, request) {
            status_url = request.getResponseHeader('Location');
            // 调用 update_progress() 方法更新进度条
            update_progress(status_url, nanobar, div[0]);
            },
            error: function() {
                alert('Unexpected error');
            }
        });
    }
    
    // 更新进度条
    function update_progress(status_url, nanobar, status_div) {
        // getJSON()方法是JQuery内置方法，这里向Location中对应的url发起请求，即请求「/status/<task_id>」
        $.getJSON(status_url, function(data) {
             // 计算进度
            percent = parseInt(data['current'] * 100 / data['total']);
            // 更新进度条
            nanobar.go(percent);
    
            // 更新文字
            $(status_div.childNodes[1]).text(percent + '%');
            $(status_div.childNodes[2]).text(data['status']);
            if (data['state'] != 'PENDING' && data['state'] != 'PROGRESS') {
                if ('result' in data) {
                // 展示结果
                    $(status_div.childNodes[3]).text('Result: ' + data['result']);
                }
                else {
                // 意料之外的事情发生
                    $(status_div.childNodes[3]).text('Result: ' + data['state']);
                }
            }
            else {
            // 2秒后再次运行
                setTimeout(function() {
                update_progress(status_url, nanobar, status_div);
                }, 2000);
            }
        });
    }
    