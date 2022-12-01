from OpenGL.GL.shaders import *
from OpenGL.GL import *
import glm

vertex_shader = """
#version 460
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 vertexColor;
uniform mat4 amatrix;
out vec3 ourColor;
void main()
{
    gl_Position = amatrix * vec4(position, 1.0f);
    ourColor = vertexColor;
}
"""

fragment_shader = """
#version 460
layout (location = 0) out vec4 fragColor;
uniform vec3 color;
in vec3 ourColor;
void main()
{
    // fragColor = vec4(ourColor, 1.0f);
    fragColor = vec4(color, 1.0f);
}
"""

def calculateMatrix(angle):
    i = glm.mat4(1)
    Translate = glm.translate(i, glm.vec3(0, 0, 0))
    Rotate = glm.rotate(i, glm.radians(angle), glm.vec3(0, 1, 0))
    Scale = glm.scale(i, glm.vec3(1, 1, 1))

    Model = Translate * Rotate * Scale

    View = glm.lookAt(
        glm.vec3(0, 0, 15),
        glm.vec3(0, 0, 0),
        glm.vec3(0, 1, 0)
    )

    Projection = glm.perspective(
        glm.radians(45),
        1600/1200,
        0.1,
        1000.0
    )

    amatrix = Projection * View * Model

    glUniformMatrix4fv(
        glGetUniformLocation(
            compileProgram(
                compileShader(fragment_shader , GL_FRAGMENT_SHADER),
                compileShader(vertex_shader, GL_VERTEX_SHADER)
            ), 
            'amatrix'
        ),
        1,
        GL_FALSE,
        glm.value_ptr(amatrix)
    )
