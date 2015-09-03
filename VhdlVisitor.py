# Generated from vhdl.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .VhdlParser import VhdlParser
else:
    from VhdlParser import VhdlParser

# This class defines a complete generic visitor for a parse tree produced by VhdlParser.

class VhdlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VhdlParser#abstract_literal.
    def visitAbstract_literal(self, ctx:VhdlParser.Abstract_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#access_type_definition.
    def visitAccess_type_definition(self, ctx:VhdlParser.Access_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#across_aspect.
    def visitAcross_aspect(self, ctx:VhdlParser.Across_aspectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#actual_designator.
    def visitActual_designator(self, ctx:VhdlParser.Actual_designatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#actual_parameter_part.
    def visitActual_parameter_part(self, ctx:VhdlParser.Actual_parameter_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#actual_part.
    def visitActual_part(self, ctx:VhdlParser.Actual_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#adding_operator.
    def visitAdding_operator(self, ctx:VhdlParser.Adding_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#aggregate.
    def visitAggregate(self, ctx:VhdlParser.AggregateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#alias_declaration.
    def visitAlias_declaration(self, ctx:VhdlParser.Alias_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#alias_designator.
    def visitAlias_designator(self, ctx:VhdlParser.Alias_designatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#alias_indication.
    def visitAlias_indication(self, ctx:VhdlParser.Alias_indicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#allocator.
    def visitAllocator(self, ctx:VhdlParser.AllocatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#architecture_body.
    def visitArchitecture_body(self, ctx:VhdlParser.Architecture_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#architecture_declarative_part.
    def visitArchitecture_declarative_part(self, ctx:VhdlParser.Architecture_declarative_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#architecture_statement.
    def visitArchitecture_statement(self, ctx:VhdlParser.Architecture_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#architecture_statement_part.
    def visitArchitecture_statement_part(self, ctx:VhdlParser.Architecture_statement_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#array_nature_definition.
    def visitArray_nature_definition(self, ctx:VhdlParser.Array_nature_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#array_type_definition.
    def visitArray_type_definition(self, ctx:VhdlParser.Array_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#assertion.
    def visitAssertion(self, ctx:VhdlParser.AssertionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#assertion_statement.
    def visitAssertion_statement(self, ctx:VhdlParser.Assertion_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#association_element.
    def visitAssociation_element(self, ctx:VhdlParser.Association_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#association_list.
    def visitAssociation_list(self, ctx:VhdlParser.Association_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#attribute_declaration.
    def visitAttribute_declaration(self, ctx:VhdlParser.Attribute_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#attribute_designator.
    def visitAttribute_designator(self, ctx:VhdlParser.Attribute_designatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#attribute_specification.
    def visitAttribute_specification(self, ctx:VhdlParser.Attribute_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#base_unit_declaration.
    def visitBase_unit_declaration(self, ctx:VhdlParser.Base_unit_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#binding_indication.
    def visitBinding_indication(self, ctx:VhdlParser.Binding_indicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#block_configuration.
    def visitBlock_configuration(self, ctx:VhdlParser.Block_configurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#block_declarative_item.
    def visitBlock_declarative_item(self, ctx:VhdlParser.Block_declarative_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#block_declarative_part.
    def visitBlock_declarative_part(self, ctx:VhdlParser.Block_declarative_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#block_header.
    def visitBlock_header(self, ctx:VhdlParser.Block_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#block_specification.
    def visitBlock_specification(self, ctx:VhdlParser.Block_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#block_statement.
    def visitBlock_statement(self, ctx:VhdlParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#block_statement_part.
    def visitBlock_statement_part(self, ctx:VhdlParser.Block_statement_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#branch_quantity_declaration.
    def visitBranch_quantity_declaration(self, ctx:VhdlParser.Branch_quantity_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#break_element.
    def visitBreak_element(self, ctx:VhdlParser.Break_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#break_list.
    def visitBreak_list(self, ctx:VhdlParser.Break_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#break_selector_clause.
    def visitBreak_selector_clause(self, ctx:VhdlParser.Break_selector_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#break_statement.
    def visitBreak_statement(self, ctx:VhdlParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#case_statement.
    def visitCase_statement(self, ctx:VhdlParser.Case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#case_statement_alternative.
    def visitCase_statement_alternative(self, ctx:VhdlParser.Case_statement_alternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#choice.
    def visitChoice(self, ctx:VhdlParser.ChoiceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#choices.
    def visitChoices(self, ctx:VhdlParser.ChoicesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#component_configuration.
    def visitComponent_configuration(self, ctx:VhdlParser.Component_configurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#component_declaration.
    def visitComponent_declaration(self, ctx:VhdlParser.Component_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#component_instantiation_statement.
    def visitComponent_instantiation_statement(self, ctx:VhdlParser.Component_instantiation_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#component_specification.
    def visitComponent_specification(self, ctx:VhdlParser.Component_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#composite_nature_definition.
    def visitComposite_nature_definition(self, ctx:VhdlParser.Composite_nature_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#composite_type_definition.
    def visitComposite_type_definition(self, ctx:VhdlParser.Composite_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#concurrent_assertion_statement.
    def visitConcurrent_assertion_statement(self, ctx:VhdlParser.Concurrent_assertion_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#concurrent_break_statement.
    def visitConcurrent_break_statement(self, ctx:VhdlParser.Concurrent_break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#concurrent_procedure_call_statement.
    def visitConcurrent_procedure_call_statement(self, ctx:VhdlParser.Concurrent_procedure_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#concurrent_signal_assignment_statement.
    def visitConcurrent_signal_assignment_statement(self, ctx:VhdlParser.Concurrent_signal_assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#condition.
    def visitCondition(self, ctx:VhdlParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#condition_clause.
    def visitCondition_clause(self, ctx:VhdlParser.Condition_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#conditional_signal_assignment.
    def visitConditional_signal_assignment(self, ctx:VhdlParser.Conditional_signal_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#conditional_waveforms.
    def visitConditional_waveforms(self, ctx:VhdlParser.Conditional_waveformsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#configuration_declaration.
    def visitConfiguration_declaration(self, ctx:VhdlParser.Configuration_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#configuration_declarative_item.
    def visitConfiguration_declarative_item(self, ctx:VhdlParser.Configuration_declarative_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#configuration_declarative_part.
    def visitConfiguration_declarative_part(self, ctx:VhdlParser.Configuration_declarative_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#configuration_item.
    def visitConfiguration_item(self, ctx:VhdlParser.Configuration_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#configuration_specification.
    def visitConfiguration_specification(self, ctx:VhdlParser.Configuration_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#constant_declaration.
    def visitConstant_declaration(self, ctx:VhdlParser.Constant_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#constrained_array_definition.
    def visitConstrained_array_definition(self, ctx:VhdlParser.Constrained_array_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#constrained_nature_definition.
    def visitConstrained_nature_definition(self, ctx:VhdlParser.Constrained_nature_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#constraint.
    def visitConstraint(self, ctx:VhdlParser.ConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#context_clause.
    def visitContext_clause(self, ctx:VhdlParser.Context_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#context_item.
    def visitContext_item(self, ctx:VhdlParser.Context_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#delay_mechanism.
    def visitDelay_mechanism(self, ctx:VhdlParser.Delay_mechanismContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#design_file.
    def visitDesign_file(self, ctx:VhdlParser.Design_fileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#design_unit.
    def visitDesign_unit(self, ctx:VhdlParser.Design_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#designator.
    def visitDesignator(self, ctx:VhdlParser.DesignatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#direction.
    def visitDirection(self, ctx:VhdlParser.DirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#disconnection_specification.
    def visitDisconnection_specification(self, ctx:VhdlParser.Disconnection_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#discrete_range.
    def visitDiscrete_range(self, ctx:VhdlParser.Discrete_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#element_association.
    def visitElement_association(self, ctx:VhdlParser.Element_associationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#element_declaration.
    def visitElement_declaration(self, ctx:VhdlParser.Element_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#element_subnature_definition.
    def visitElement_subnature_definition(self, ctx:VhdlParser.Element_subnature_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#element_subtype_definition.
    def visitElement_subtype_definition(self, ctx:VhdlParser.Element_subtype_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#entity_aspect.
    def visitEntity_aspect(self, ctx:VhdlParser.Entity_aspectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#entity_class.
    def visitEntity_class(self, ctx:VhdlParser.Entity_classContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#entity_class_entry.
    def visitEntity_class_entry(self, ctx:VhdlParser.Entity_class_entryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#entity_class_entry_list.
    def visitEntity_class_entry_list(self, ctx:VhdlParser.Entity_class_entry_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#entity_declaration.
    def visitEntity_declaration(self, ctx:VhdlParser.Entity_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#entity_declarative_item.
    def visitEntity_declarative_item(self, ctx:VhdlParser.Entity_declarative_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#entity_declarative_part.
    def visitEntity_declarative_part(self, ctx:VhdlParser.Entity_declarative_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#entity_designator.
    def visitEntity_designator(self, ctx:VhdlParser.Entity_designatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#entity_header.
    def visitEntity_header(self, ctx:VhdlParser.Entity_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#entity_name_list.
    def visitEntity_name_list(self, ctx:VhdlParser.Entity_name_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#entity_specification.
    def visitEntity_specification(self, ctx:VhdlParser.Entity_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#entity_statement.
    def visitEntity_statement(self, ctx:VhdlParser.Entity_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#entity_statement_part.
    def visitEntity_statement_part(self, ctx:VhdlParser.Entity_statement_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#entity_tag.
    def visitEntity_tag(self, ctx:VhdlParser.Entity_tagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#enumeration_literal.
    def visitEnumeration_literal(self, ctx:VhdlParser.Enumeration_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#enumeration_type_definition.
    def visitEnumeration_type_definition(self, ctx:VhdlParser.Enumeration_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#exit_statement.
    def visitExit_statement(self, ctx:VhdlParser.Exit_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#expression.
    def visitExpression(self, ctx:VhdlParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#factor.
    def visitFactor(self, ctx:VhdlParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#file_declaration.
    def visitFile_declaration(self, ctx:VhdlParser.File_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#file_logical_name.
    def visitFile_logical_name(self, ctx:VhdlParser.File_logical_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#file_open_information.
    def visitFile_open_information(self, ctx:VhdlParser.File_open_informationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#file_type_definition.
    def visitFile_type_definition(self, ctx:VhdlParser.File_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#formal_parameter_list.
    def visitFormal_parameter_list(self, ctx:VhdlParser.Formal_parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#formal_part.
    def visitFormal_part(self, ctx:VhdlParser.Formal_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#free_quantity_declaration.
    def visitFree_quantity_declaration(self, ctx:VhdlParser.Free_quantity_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#generate_statement.
    def visitGenerate_statement(self, ctx:VhdlParser.Generate_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#generation_scheme.
    def visitGeneration_scheme(self, ctx:VhdlParser.Generation_schemeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#generic_clause.
    def visitGeneric_clause(self, ctx:VhdlParser.Generic_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#generic_list.
    def visitGeneric_list(self, ctx:VhdlParser.Generic_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#generic_map_aspect.
    def visitGeneric_map_aspect(self, ctx:VhdlParser.Generic_map_aspectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#group_constituent.
    def visitGroup_constituent(self, ctx:VhdlParser.Group_constituentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#group_constituent_list.
    def visitGroup_constituent_list(self, ctx:VhdlParser.Group_constituent_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#group_declaration.
    def visitGroup_declaration(self, ctx:VhdlParser.Group_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#group_template_declaration.
    def visitGroup_template_declaration(self, ctx:VhdlParser.Group_template_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#guarded_signal_specification.
    def visitGuarded_signal_specification(self, ctx:VhdlParser.Guarded_signal_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#identifier.
    def visitIdentifier(self, ctx:VhdlParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#identifier_list.
    def visitIdentifier_list(self, ctx:VhdlParser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#if_statement.
    def visitIf_statement(self, ctx:VhdlParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#index_constraint.
    def visitIndex_constraint(self, ctx:VhdlParser.Index_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#index_specification.
    def visitIndex_specification(self, ctx:VhdlParser.Index_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#index_subtype_definition.
    def visitIndex_subtype_definition(self, ctx:VhdlParser.Index_subtype_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#instantiated_unit.
    def visitInstantiated_unit(self, ctx:VhdlParser.Instantiated_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#instantiation_list.
    def visitInstantiation_list(self, ctx:VhdlParser.Instantiation_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#interface_constant_declaration.
    def visitInterface_constant_declaration(self, ctx:VhdlParser.Interface_constant_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#interface_declaration.
    def visitInterface_declaration(self, ctx:VhdlParser.Interface_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#interface_element.
    def visitInterface_element(self, ctx:VhdlParser.Interface_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#interface_file_declaration.
    def visitInterface_file_declaration(self, ctx:VhdlParser.Interface_file_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#interface_signal_list.
    def visitInterface_signal_list(self, ctx:VhdlParser.Interface_signal_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#interface_port_list.
    def visitInterface_port_list(self, ctx:VhdlParser.Interface_port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#interface_list.
    def visitInterface_list(self, ctx:VhdlParser.Interface_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#interface_quantity_declaration.
    def visitInterface_quantity_declaration(self, ctx:VhdlParser.Interface_quantity_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#interface_port_declaration.
    def visitInterface_port_declaration(self, ctx:VhdlParser.Interface_port_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#interface_signal_declaration.
    def visitInterface_signal_declaration(self, ctx:VhdlParser.Interface_signal_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#interface_terminal_declaration.
    def visitInterface_terminal_declaration(self, ctx:VhdlParser.Interface_terminal_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#interface_variable_declaration.
    def visitInterface_variable_declaration(self, ctx:VhdlParser.Interface_variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#iteration_scheme.
    def visitIteration_scheme(self, ctx:VhdlParser.Iteration_schemeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#label_colon.
    def visitLabel_colon(self, ctx:VhdlParser.Label_colonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#library_clause.
    def visitLibrary_clause(self, ctx:VhdlParser.Library_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#library_unit.
    def visitLibrary_unit(self, ctx:VhdlParser.Library_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#literal.
    def visitLiteral(self, ctx:VhdlParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#logical_name.
    def visitLogical_name(self, ctx:VhdlParser.Logical_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#logical_name_list.
    def visitLogical_name_list(self, ctx:VhdlParser.Logical_name_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#logical_operator.
    def visitLogical_operator(self, ctx:VhdlParser.Logical_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#loop_statement.
    def visitLoop_statement(self, ctx:VhdlParser.Loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#signal_mode.
    def visitSignal_mode(self, ctx:VhdlParser.Signal_modeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#multiplying_operator.
    def visitMultiplying_operator(self, ctx:VhdlParser.Multiplying_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#name.
    def visitName(self, ctx:VhdlParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#name_part.
    def visitName_part(self, ctx:VhdlParser.Name_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#name_attribute_part.
    def visitName_attribute_part(self, ctx:VhdlParser.Name_attribute_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#name_function_call_or_indexed_part.
    def visitName_function_call_or_indexed_part(self, ctx:VhdlParser.Name_function_call_or_indexed_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#name_slice_part.
    def visitName_slice_part(self, ctx:VhdlParser.Name_slice_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#selected_name.
    def visitSelected_name(self, ctx:VhdlParser.Selected_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#nature_declaration.
    def visitNature_declaration(self, ctx:VhdlParser.Nature_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#nature_definition.
    def visitNature_definition(self, ctx:VhdlParser.Nature_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#nature_element_declaration.
    def visitNature_element_declaration(self, ctx:VhdlParser.Nature_element_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#next_statement.
    def visitNext_statement(self, ctx:VhdlParser.Next_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#numeric_literal.
    def visitNumeric_literal(self, ctx:VhdlParser.Numeric_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#object_declaration.
    def visitObject_declaration(self, ctx:VhdlParser.Object_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#opts.
    def visitOpts(self, ctx:VhdlParser.OptsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#package_body.
    def visitPackage_body(self, ctx:VhdlParser.Package_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#package_body_declarative_item.
    def visitPackage_body_declarative_item(self, ctx:VhdlParser.Package_body_declarative_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#package_body_declarative_part.
    def visitPackage_body_declarative_part(self, ctx:VhdlParser.Package_body_declarative_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#package_declaration.
    def visitPackage_declaration(self, ctx:VhdlParser.Package_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#package_declarative_item.
    def visitPackage_declarative_item(self, ctx:VhdlParser.Package_declarative_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#package_declarative_part.
    def visitPackage_declarative_part(self, ctx:VhdlParser.Package_declarative_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#parameter_specification.
    def visitParameter_specification(self, ctx:VhdlParser.Parameter_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#physical_literal.
    def visitPhysical_literal(self, ctx:VhdlParser.Physical_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#physical_type_definition.
    def visitPhysical_type_definition(self, ctx:VhdlParser.Physical_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#port_clause.
    def visitPort_clause(self, ctx:VhdlParser.Port_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#port_list.
    def visitPort_list(self, ctx:VhdlParser.Port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#port_map_aspect.
    def visitPort_map_aspect(self, ctx:VhdlParser.Port_map_aspectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#primary.
    def visitPrimary(self, ctx:VhdlParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#primary_unit.
    def visitPrimary_unit(self, ctx:VhdlParser.Primary_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#procedural_declarative_item.
    def visitProcedural_declarative_item(self, ctx:VhdlParser.Procedural_declarative_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#procedural_declarative_part.
    def visitProcedural_declarative_part(self, ctx:VhdlParser.Procedural_declarative_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#procedural_statement_part.
    def visitProcedural_statement_part(self, ctx:VhdlParser.Procedural_statement_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#procedure_call.
    def visitProcedure_call(self, ctx:VhdlParser.Procedure_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#procedure_call_statement.
    def visitProcedure_call_statement(self, ctx:VhdlParser.Procedure_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#process_declarative_item.
    def visitProcess_declarative_item(self, ctx:VhdlParser.Process_declarative_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#process_declarative_part.
    def visitProcess_declarative_part(self, ctx:VhdlParser.Process_declarative_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#process_statement.
    def visitProcess_statement(self, ctx:VhdlParser.Process_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#process_statement_part.
    def visitProcess_statement_part(self, ctx:VhdlParser.Process_statement_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#qualified_expression.
    def visitQualified_expression(self, ctx:VhdlParser.Qualified_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#quantity_declaration.
    def visitQuantity_declaration(self, ctx:VhdlParser.Quantity_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#quantity_list.
    def visitQuantity_list(self, ctx:VhdlParser.Quantity_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#quantity_specification.
    def visitQuantity_specification(self, ctx:VhdlParser.Quantity_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#range_base.
    def visitRange_base(self, ctx:VhdlParser.Range_baseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#explicit_range.
    def visitExplicit_range(self, ctx:VhdlParser.Explicit_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#range_constraint.
    def visitRange_constraint(self, ctx:VhdlParser.Range_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#record_nature_definition.
    def visitRecord_nature_definition(self, ctx:VhdlParser.Record_nature_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#record_type_definition.
    def visitRecord_type_definition(self, ctx:VhdlParser.Record_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#relation.
    def visitRelation(self, ctx:VhdlParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#relational_operator.
    def visitRelational_operator(self, ctx:VhdlParser.Relational_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#report_statement.
    def visitReport_statement(self, ctx:VhdlParser.Report_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#return_statement.
    def visitReturn_statement(self, ctx:VhdlParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#scalar_nature_definition.
    def visitScalar_nature_definition(self, ctx:VhdlParser.Scalar_nature_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#scalar_type_definition.
    def visitScalar_type_definition(self, ctx:VhdlParser.Scalar_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#secondary_unit.
    def visitSecondary_unit(self, ctx:VhdlParser.Secondary_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#secondary_unit_declaration.
    def visitSecondary_unit_declaration(self, ctx:VhdlParser.Secondary_unit_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#selected_signal_assignment.
    def visitSelected_signal_assignment(self, ctx:VhdlParser.Selected_signal_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#selected_waveforms.
    def visitSelected_waveforms(self, ctx:VhdlParser.Selected_waveformsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#sensitivity_clause.
    def visitSensitivity_clause(self, ctx:VhdlParser.Sensitivity_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#sensitivity_list.
    def visitSensitivity_list(self, ctx:VhdlParser.Sensitivity_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#sequence_of_statements.
    def visitSequence_of_statements(self, ctx:VhdlParser.Sequence_of_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#sequential_statement.
    def visitSequential_statement(self, ctx:VhdlParser.Sequential_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#shift_expression.
    def visitShift_expression(self, ctx:VhdlParser.Shift_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#shift_operator.
    def visitShift_operator(self, ctx:VhdlParser.Shift_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#signal_assignment_statement.
    def visitSignal_assignment_statement(self, ctx:VhdlParser.Signal_assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#signal_declaration.
    def visitSignal_declaration(self, ctx:VhdlParser.Signal_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#signal_kind.
    def visitSignal_kind(self, ctx:VhdlParser.Signal_kindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#signal_list.
    def visitSignal_list(self, ctx:VhdlParser.Signal_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#signature.
    def visitSignature(self, ctx:VhdlParser.SignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#simple_expression.
    def visitSimple_expression(self, ctx:VhdlParser.Simple_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#simple_simultaneous_statement.
    def visitSimple_simultaneous_statement(self, ctx:VhdlParser.Simple_simultaneous_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#simultaneous_alternative.
    def visitSimultaneous_alternative(self, ctx:VhdlParser.Simultaneous_alternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#simultaneous_case_statement.
    def visitSimultaneous_case_statement(self, ctx:VhdlParser.Simultaneous_case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#simultaneous_if_statement.
    def visitSimultaneous_if_statement(self, ctx:VhdlParser.Simultaneous_if_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#simultaneous_procedural_statement.
    def visitSimultaneous_procedural_statement(self, ctx:VhdlParser.Simultaneous_procedural_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#simultaneous_statement.
    def visitSimultaneous_statement(self, ctx:VhdlParser.Simultaneous_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#simultaneous_statement_part.
    def visitSimultaneous_statement_part(self, ctx:VhdlParser.Simultaneous_statement_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#source_aspect.
    def visitSource_aspect(self, ctx:VhdlParser.Source_aspectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#source_quantity_declaration.
    def visitSource_quantity_declaration(self, ctx:VhdlParser.Source_quantity_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#step_limit_specification.
    def visitStep_limit_specification(self, ctx:VhdlParser.Step_limit_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#subnature_declaration.
    def visitSubnature_declaration(self, ctx:VhdlParser.Subnature_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#subnature_indication.
    def visitSubnature_indication(self, ctx:VhdlParser.Subnature_indicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#subprogram_body.
    def visitSubprogram_body(self, ctx:VhdlParser.Subprogram_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#subprogram_declaration.
    def visitSubprogram_declaration(self, ctx:VhdlParser.Subprogram_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#subprogram_declarative_item.
    def visitSubprogram_declarative_item(self, ctx:VhdlParser.Subprogram_declarative_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#subprogram_declarative_part.
    def visitSubprogram_declarative_part(self, ctx:VhdlParser.Subprogram_declarative_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#subprogram_kind.
    def visitSubprogram_kind(self, ctx:VhdlParser.Subprogram_kindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#subprogram_specification.
    def visitSubprogram_specification(self, ctx:VhdlParser.Subprogram_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#procedure_specification.
    def visitProcedure_specification(self, ctx:VhdlParser.Procedure_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#function_specification.
    def visitFunction_specification(self, ctx:VhdlParser.Function_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#subprogram_statement_part.
    def visitSubprogram_statement_part(self, ctx:VhdlParser.Subprogram_statement_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#subtype_declaration.
    def visitSubtype_declaration(self, ctx:VhdlParser.Subtype_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#subtype_indication.
    def visitSubtype_indication(self, ctx:VhdlParser.Subtype_indicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#suffix.
    def visitSuffix(self, ctx:VhdlParser.SuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#target.
    def visitTarget(self, ctx:VhdlParser.TargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#term.
    def visitTerm(self, ctx:VhdlParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#terminal_aspect.
    def visitTerminal_aspect(self, ctx:VhdlParser.Terminal_aspectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#terminal_declaration.
    def visitTerminal_declaration(self, ctx:VhdlParser.Terminal_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#through_aspect.
    def visitThrough_aspect(self, ctx:VhdlParser.Through_aspectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#timeout_clause.
    def visitTimeout_clause(self, ctx:VhdlParser.Timeout_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#tolerance_aspect.
    def visitTolerance_aspect(self, ctx:VhdlParser.Tolerance_aspectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#type_declaration.
    def visitType_declaration(self, ctx:VhdlParser.Type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#type_definition.
    def visitType_definition(self, ctx:VhdlParser.Type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#unconstrained_array_definition.
    def visitUnconstrained_array_definition(self, ctx:VhdlParser.Unconstrained_array_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#unconstrained_nature_definition.
    def visitUnconstrained_nature_definition(self, ctx:VhdlParser.Unconstrained_nature_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#use_clause.
    def visitUse_clause(self, ctx:VhdlParser.Use_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#variable_assignment_statement.
    def visitVariable_assignment_statement(self, ctx:VhdlParser.Variable_assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#variable_declaration.
    def visitVariable_declaration(self, ctx:VhdlParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#wait_statement.
    def visitWait_statement(self, ctx:VhdlParser.Wait_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#waveform.
    def visitWaveform(self, ctx:VhdlParser.WaveformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VhdlParser#waveform_element.
    def visitWaveform_element(self, ctx:VhdlParser.Waveform_elementContext):
        return self.visitChildren(ctx)



del VhdlParser