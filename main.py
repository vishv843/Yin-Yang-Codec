from yyc import pipeline
from yyc import scheme

#encode
def encoding(inputFilePath,outputFilePath):
    pipeline.encode(method=scheme.YYC(support_bases="A", base_reference=[0, 1, 0, 1], current_code_matrix=[[1, 1, 0, 0], [1, 0, 0, 1], [1, 1, 0, 0], [1, 1, 0, 0]], search_count=100, max_homopolymer=4, max_content=0.6), input_path=inputFilePath, output_path=outputFilePath+"/OutputFile.dna", model_path=outputFilePath+"/yyc.pkl", need_index=True, need_log=True)

#decode
def decoding(inputFilePath, outputFilePath):
    pipeline.decode(model_path=outputFilePath+"/yyc.pkl",input_path=inputFilePath, output_path=outputFilePath+"/output.png", has_index=True, need_log=True)