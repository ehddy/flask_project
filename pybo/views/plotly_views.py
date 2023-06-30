from datetime import datetime

from flask import Blueprint, url_for, render_template
import plotly.graph_objs as go


bp = Blueprint('plotly', __name__, url_prefix='/plot')


@bp.route('/plotly')
def create():
     # 그래프 데이터 생성
    data = [
        go.Bar(
            x=['A', 'B', 'C'],
            y=[3, 4, 1]
        )
    ]

    # 그래프 레이아웃 설정
    layout = go.Layout(
        title='Sample Bar Chart',
        xaxis=dict(title='X-axis'),
        yaxis=dict(title='Y-axis')
    )

    # 그래프 객체 생성
    fig = go.Figure(data=data, layout=layout)

    # HTML 템플릿에 그래프를 표시하기 위해 그래프 객체를 JSON으로 변환
    graphJSON = fig.to_json()

    # index.html 템플릿 렌더링 및 그래프 데이터 전달
    return render_template('plotly/plotly.html', graphJSON=graphJSON)