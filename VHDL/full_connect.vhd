LIBRARY IEEE;
USE ieee.std_logic_1164.ALL;
USE work.parameters.ALL;

ENTITY full_connect IS
PORT(
	input 				: IN  input_image;
	weight 				: IN  array_weight;
	clock					: IN  STD_LOGIC;
	reset					: IN  STD_LOGIC;
	output 				: OUT array_multiplier
);
END full_connect;

ARCHITECTURE behavior OF full_connect IS
SIGNAL out_layer_1 : input_image;
SIGNAL out_layer_2 : input_image;

SIGNAL input_temp : input_image;
--SIGNAL weight_temp : input_image (ad asd);

COMPONENT perceptron IS
PORT(
	input       			: IN  input_image;
	weight 					: IN  input_image;
	layer_indentifier		: IN  STD_LOGIC_VECTOR(1 DOWNTO 0);
	clock						: IN  STD_LOGIC;
	reset		   			: IN  STD_LOGIC;
	output 					: OUT STD_LOGIC_VECTOR((2 + precision) DOWNTO 0)
);		
END COMPONENT;
BEGIN

--weight_transfer:
--	FOR i IN 0 TO ((data_width * n_perceptrons) - 1) GENERATE
--		weight_temp(i) <= weight(i);
--	END GENERATE weight_transfer;

layer_1:
	FOR i IN 1 TO n_perceptrons_1 GENERATE		
		Neurons_layer_1: perceptron 
			PORT MAP(input, weight(i-1), "00", clock, reset, out_layer_1(i-1));
	
	END GENERATE layer_1;

layer_2:
	FOR i IN 1 TO n_perceptrons_2 GENERATE
		Neurons_layer_2: perceptron 
			PORT MAP(out_layer_1, weight(n_perceptrons_2 + i - 1), "01", clock, reset, out_layer_2(i-1));
	
	END GENERATE layer_2;
	
layer_output:
	FOR i IN 1 TO n_perceptrons_output GENERATE
		Neurons_layer_output: perceptron 
			PORT MAP(out_layer_2, weight(n_perceptrons_output + i - 1), "10", clock, reset, output(i-1));
	
	END GENERATE layer_output;
	
END behavior;