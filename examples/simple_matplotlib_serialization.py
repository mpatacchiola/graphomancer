import matplotlib.pyplot as plt
from graphomancer.serializers.matplotlib.line_serializer import LinePlotMatplotlibSerializer

fig, ax = plt.subplots()
ax.plot([2000, 2001, 2002], [1.5, 1.8, 2.0], label="USA")
ax.plot([2000, 2001, 2002], [1.2, 1.4, 1.6], label="Germany")

serializer = LinePlotMatplotlibSerializer(fig, theme="dark", description="GDP over years", source="World Bank")
schema = serializer.serialize()

print(schema.model_dump_json(indent=2))